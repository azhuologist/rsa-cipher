"""Runs tests on the main application."""


import unittest
import os
import filecmp
import RSACipher

class BasicTests(unittest.TestCase):

    def test_image(self):
        """Runs encryption and then decryption on a small PNG file."""
        ciph = RSACipher.RSACipher()
        ciph.encrypt('resources/test/Wallpaper.png', 'encryptedimage.png')
        ciph.decrypt('encryptedimage.png', 'result.png')

        self.assertTrue(filecmp.cmp('resources/test/Wallpaper.png', 'result.png'))

    def tearDown(self):
        os.remove('encryptedimage.png')
        os.remove('result.png')

if __name__ == '__main__':
    unittest.main()
