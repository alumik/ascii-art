import unittest

from PIL import Image

import ascii_art


class AsciiArtTestCase(unittest.TestCase):

    @staticmethod
    def test_ascii_art():
        image = Image.open('resources/img.png')
        image = ascii_art.to_grayscale(image)
        art = ascii_art.make_art(image)
        ascii_art.print_art(art)
