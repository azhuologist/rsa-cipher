"""Runs tests on the main application."""


import unittest
import filecmp
import RSACipher

ciph = RSACipher.RSACipher()
ciph.encrypt('IMG_1559.jpg', 'encryptedimage.jpg')
ciph.decrypt('encryptedimage.jpg', 'result.jpg')

if filecmp.cmp('IMG_1559.jpg', 'result.jpg'):
    print('Success!')

class BasicTests(unittest.TestCase):
    pass
    