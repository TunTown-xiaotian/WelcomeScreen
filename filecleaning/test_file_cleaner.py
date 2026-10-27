import os
import shutil
import unittest
from pathlib import Path
from FileCleaner import file_cleanup

class TestFileCleanup(unittest.TestCase):
    def setUp(self):
        self.base_dir = Path(__file__).parent
        self.target_dir = os.path.join(self.base_dir, 'temporary_file')
        os.makedirs(self.target_dir, exist_ok=True)

        with open(os.path.join(self.target_dir, 'helloa.txt'), 'w') as f:
            f.write('123456')
        with open(os.path.join(self.target_dir, 'hellob.txt'), 'w') as f:
            f.write('123456')
        with open(os.path.join(self.target_dir, 'helloc.txt'), 'w') as f:
            f.write('123456')

    def tearDown(self):
        shutil.rmtree(self.target_dir)

    def test_file_cleanup(self):
        count = file_cleanup(self.target_dir)
        self.assertEqual(count, 3)

if __name__ == "__main__":
    unittest.main()


