# rsa-cipher
A command line application that encrypts files with 1024-bit RSA, tested on Windows machines only. Work in progress.

Usage
-----

To encrypt a file and write encrypted data to an output file with a randomly generated key pair:

```bash
> RSACipher.py new encrypt sourcefile.txt output.txt
```

To load an existing cipher:

```bash
> RSACipher.py cipher.txt encrypt sourcefile.txt output.txt
```
