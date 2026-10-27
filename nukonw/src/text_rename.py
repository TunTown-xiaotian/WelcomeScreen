import os.path
import shutil
import unittest
from pathlib import Path
from get_new_filename import batch_rename_files


class TestBatchFileRename(unittest.TestCase):
    def setUp(self):
        base_path = Path(__file__).parent
        image_dir_path = os.path.join(base_path,"images")
        os.mkdir(image_dir_path)

        for num in range(1,6):
            image_path = os.path.join(image_dir_path,f"photo{num}.jpg")
            with open(image_path,"w") as file:
                pass

    def test_batch_rename(self):
        self.assertEqual(batch_rename_files(),5)

    def tearDown(self):
        base_path = Path(__file__).parent
        image_dir_path = os.path.join(base_path, "images")
        shutil.rmtree(image_dir_path)

    def back_dir(self):
        self.assertEqual(backup_dir(),)

    if __name__ == "__main__":
        unittest.main()
