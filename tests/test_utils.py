import unittest

from musixmatch import _set_page_size


class TestUtils(unittest.TestCase):

    def test_set_page_size(self):
        self.assertEqual(_set_page_size(200), 100)
        self.assertEqual(_set_page_size(-10), 1)
        self.assertEqual(_set_page_size(10), 10)


if __name__ == '__main__':
    unittest.main()
