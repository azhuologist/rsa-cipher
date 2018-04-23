"""Runs tests on the main application."""


import unittest
import os
import filecmp
import RSACipher

class BasicTests(unittest.TestCase):
    """Tests different aspects of the RSA protocol."""

    def test_text_file(self):
        """Tests encryption / decryption on a TXT text file."""
        ciph = RSACipher.RSACipher()
        ciph.encrypt('resources/test/dorian_gray.txt', 'encryptedtext.txt')
        ciph.decrypt('encryptedtext.txt', 'result.txt')

        self.assertTrue(filecmp.cmp('resources/test/dorian_gray.txt', 'result.txt'))


    def test_image(self):
        """Tests encryption / decryption on a small PNG image file."""
        ciph = RSACipher.RSACipher()
        ciph.encrypt('resources/test/Wallpaper.png', 'encryptedimage.png')
        ciph.decrypt('encryptedimage.png', 'result.png')

        self.assertTrue(filecmp.cmp('resources/test/Wallpaper.png', 'result.png'))

    def test_read_keys(self):
        """Tests the ability to save keys to and read keys from a file."""
        random_keys = RSACipher.RSACipher()
        random_keys.save('savedkeys.txt')
        loaded_keys = RSACipher.RSACipher('savedkeys.txt')
        self.assertEqual(random_keys.n, loaded_keys.n, 'Modulus not saved/loaded correctly')
        self.assertEqual(random_keys.encrypt_key, loaded_keys.encrypt_key, 'Public key not saved/loaded correctly')
        self.assertEqual(random_keys.decrypt_key, loaded_keys.decrypt_key, 'Private key not saved/loaded correctly')

    @classmethod
    def tearDownClass(cls):
        os.remove('encryptedtext.txt')
        os.remove('result.txt')
        os.remove('encryptedimage.png')
        os.remove('result.png')
        os.remove('savedkeys.txt')

if __name__ == '__main__':
    unittest.main()
