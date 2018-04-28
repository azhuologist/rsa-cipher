# rsa-cipher
A command line application that encrypts files with 1024-bit RSA, tested on Windows machines only.

Usage
-----

To encrypt a file:

```bash
> python RSACipher.py encrypt sourcefile.txt output.txt
```

To decrypt a file:

```bash
> python RSACipher.py decrypt sourcefile.txt output.txt
```

You can save a newly created key-pair by adding `--save [keyfile]` to the beginning of your command:

```bash
> python RSACipher.py --save keys.txt decrypt sourcefile.txt output.txt
```

You can then load and use this key-pair by adding `--load [keyfile]` to the beginning of your command:

```bash
> RSACipher.py --load keys.txt decrypt sourcefile.txt output.txt
```

TODOs
-----
* Do comprehensive tests to ensure complete functionality
