import unittest

from gutenberg import GutenbergAPI


class TestSimple(unittest.TestCase):
    def test_alwaystrue(self):
        self.assertEqual(1, 1)

    def test_instance_is_default(self):
        gb = GutenbergAPI()
        self.assertEqual(gb.instance_url, "https://gutendex.devbranch.co")


if __name__ == "__main__":
    unittest.main()
