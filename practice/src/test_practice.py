import unittest
from practice.src.specific_practice import read_file


class TestReadFile(unittest.TestCase):
    def test_file_normal(self):

        def test_file_not_found_error(self):
            with self.assertRaises(FileNotFoundError):
                read_file("poem.txt")

if __name__=='__main__':
    unittest.main()