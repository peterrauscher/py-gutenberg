import unittest

from gutenberg.gutenberg import GutenbergAPI


class TestSimple(unittest.TestCase):
    def test_alwaystrue(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
