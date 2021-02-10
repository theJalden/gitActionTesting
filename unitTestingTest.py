# Python unittest testing

import unittest

class Mastodon:
    def __init__(self):
        self.legs = 4
        self.trunkLength = 2.3

    def amputate(self):
        if (self.legs > 0):
            self.legs -= 1

class TestMastodon(unittest.TestCase):
    def test_init(self):
        testoDon = Mastodon()
        self.assertEqual(testoDon.legs, 4)

    def test_amputate(self):
        testoDon = Mastodon()
        testoDon.amputate()
        self.assertEqual(testoDon.legs, 3)
        testoDon.amputate()
        self.assertEqual(testoDon.legs, 2)
        testoDon.amputate()
        self.assertEqual(testoDon.legs, 1)
        testoDon.amputate()
        self.assertEqual(testoDon.legs, 0)
        testoDon.amputate()git
        self.assertEqual(testoDon.legs, -1)


if __name__ == "__main__":
    unittest.main()