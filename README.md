# rsa-cipher
A command line application that encrypts files with 1024-bit RSA. Uses the [`number`](https://www.dlitz.net/software/pycrypto/api/current/Crypto.Util.number-module.html) class from `Crypto.Util` to generate primes.

Usage
-----

To encrypt a file:

```bash
python RSACipher.py encrypt [sourcefile] [output]
```

To decrypt a file:

```bash
python RSACipher.py decrypt [sourcefile] [output]
```

You can save a newly created key-pair by adding `--save [keyfile]` to the beginning of your command:

```bash
python RSACipher.py --save [keyfile] decrypt [sourcefile] [outputfile]
```

You can then load and use this key-pair by adding `--load [keyfile]` to the beginning of your command:

```bash
RSACipher.py --load [keyfile] decrypt [sourcefile] [outputfile]
```
