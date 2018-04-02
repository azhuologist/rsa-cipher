"""Runs tests on the main application."""


import unittest
import os
import filecmp
import RSACipher

ciph = RSACipher.RSACipher()
ciph.encrypt('resources/test/Wallpaper.png', 'encryptedimage.png')
ciph.decrypt('encryptedimage.png', 'result.png')

if filecmp.cmp('resources/test/Wallpaper.png', 'result.png'):
    print('Success!')

os.remove('encryptedimage.png')
os.remove('result.png')

class BasicTests(unittest.TestCase):
    pass
    