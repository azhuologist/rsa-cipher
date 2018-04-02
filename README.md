# rsa-cipher
A command line application that encrypts files with 1024-bit RSA, tested on Windows machines only. Work in progress.

Usage
-----

To encrypt a file and write encrypted data to an output file with a randomly generated key-pair:

```bash
> RSACipher.py new encrypt sourcefile.txt output.txt
```

To load an existing key-pair:

```bash
> RSACipher.py keys.txt decrypt sourcefile.txt output.txt
```

To save a newly created key-pair, add `--save [keyfile]` to the end of your command.

TODOs
-----


