"""Encrypts files with 512-bit RSA."""


import argparse
from Crypto.Util import number


# Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    """Perform Euclid's greatest common divisor algorithm."""
    if a == 0:
        return (b, 0, 1)

    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


# Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
    """Performs the mathematical operation (1 / a) % m."""
    values = egcd(a, m)
    if values[0] != 1:
        raise Exception('modular inverse does not exist')
    else:
        return values[1] % m


class RSACipher(object):
    """Creates an RSA cipher with randomly generated keys."""
    def __init__(self, filename = None):
        if filename is None:
            prime_one = number.getPrime(510)
            prime_two = number.getPrime(510)
            totient = (prime_one - 1) * (prime_two - 1)
            self.n = prime_one * prime_two
            self.encrypt_key = number.getPrime(255)
            self.decrypt_key = modinv(self.encrypt_key, totient)
        else:
            with open(filename, 'r') as source:
                self.n = int(source.readline())
                self.encrypt_key = int(source.readline())
                self.decrypt_key = int(source.readline())

        self.cipher_key = '%d\n%d\n%d' % (self.n, self.encrypt_key, self.decrypt_key)

    def encrypt(self, source_file, destination_file):
        """Encrypts bytes from source_file and writes the encrypted bytes to destination_file."""
        with open(source_file, 'rb') as source:
            reader = RSAReader(source)
            with open(destination_file, 'wb') as dest:
                while reader.has_next():
                    raw_bytes = reader.next_encryption_chunk()
                    chunk = int.from_bytes(raw_bytes, 'big')
                    encrypted_chunk = pow(chunk, self.encrypt_key, self.n)
                    encrypted_bytes = bytearray(encrypted_chunk.to_bytes(128, 'big'))

                    if len(encrypted_bytes) < 128:
                        padding = bytes([0] * (128 - len(encrypted_bytes)))
                        encrypted_bytes = padding + encrypted_bytes
                    dest.write(encrypted_bytes)

    def decrypt(self, source_file, destination_file):
        """Decrypts encrypted bytes from source_file and writes decrypted bytes to destination_file."""
        with open(source_file, 'rb') as source:
            reader = RSAReader(source)
            with open(destination_file, 'wb') as dest:
                while reader.has_next():
                    chunk = int.from_bytes(reader.next_decryption_chunk(), 'big')
                    decrypted_chunk = pow(chunk, self.decrypt_key, self.n)
                    decrypted_bytes = bytearray(decrypted_chunk.to_bytes(decrypted_chunk.bit_length() // 8 + 1, 'big'))

                    num_data_bytes = decrypted_bytes[0]
                    data_bytes = decrypted_bytes[1:num_data_bytes + 1]
                    dest.write(data_bytes)

    def save(self, output_file):
        """Saves this cipher's keys to output_file."""
        with open(output_file, 'w') as dest:
            dest.write(self.cipher_key)



class RSAReader:
    """Reads data from a source file to be encrypted."""
    def __init__(self, reader):
        self.reader = reader

    def has_next(self):
        """Returns a boolean describing whether the reader has reached EOF"""
        return len(self.reader.peek()) > 0

    def next_encryption_chunk(self):
        """Fetches the next chunk of bytes from the file for encryption."""
        data_bytes = bytearray(self.reader.read(126))
        length_byte = bytearray(bytes([len(data_bytes)]))
        chunk = length_byte + data_bytes

        if len(data_bytes) < 126:
            padding = bytearray(126 - len(data_bytes))
            chunk += padding

        assert len(chunk) == 127  # sanity check
        return chunk

    def next_decryption_chunk(self):
        """Fetches the next chunk of bytes from the file for encryption."""
        return bytearray(self.reader.read(128))


def main():
    """A basic command-line user interface."""
    parser = argparse.ArgumentParser()
    # TODO: fix help message formatting, add option argument groups
    parser.add_argument("cipher", type = str, help = "\'new\' to generate a new cipher with random keys,"
                                                     "\n\'[filename]\' to load an existing one")
    parser.add_argument("action", type = str, help = "\'encrypt\' or \'decrypt\'",
                        choices = ["encrypt", "en", "decrypt", "de"])
    parser.add_argument("inputfile", type = str, help = "source file to encrypt or decrypt")
    parser.add_argument("outputfile", type = str, help = "file to write to")
    parser.add_argument("--save", type = str, help = "file to save to", nargs = 1)
    args = parser.parse_args()

    if args.cipher == "new":
        cipher = RSACipher()
    else:
        cipher = RSACipher(args.cipher)

    # TODO: add exception catching
    if args.action == "encrypt" or args.action == "en":
        cipher.encrypt(args.inputfile, args.outputfile)
    elif args.action == "decrypt" or args.action == "de":
        cipher.decrypt(args.inputfile, args.outputfile)
    else:
        print("This shouldn't have happened.")



if __name__ == "__main__":
    main()
