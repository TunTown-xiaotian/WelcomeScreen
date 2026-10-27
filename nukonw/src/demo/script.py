import datetime
import os
import shutil
import unittest


def list_dir_info(path):
    if not os.path.exists(path):
        print('path does not exist')
        return []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.startswith('test_example'):
            m_time = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
            files.append(f"path: {item_path} size: {os.path.getsize(item_path)}bytes mtime: {m_time}")
    return files

def find_big_files(path, min_size):
    if not os.path.exists(path):
        print('path does not exist')
        return
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            file_size = os.path.getsize(item_path)
            if file_size > min_size:
                print(f"path: {item_path} size: {file_size}bytes")

def  safe_remove_tree(path):
    if not os.path.isdir(path):
        print(f'{path}不是目录，不能删除')
        return
    if not os.path.isfile(path):
        print(f'{path}不是文件路径，不能删除')
    if path in ('/','','.'):
        raise ValueError('拒绝删除')
    os.rmdir(path)
def test_safe_remove_tree(self):
    assert safe_remove_tree('../area.py') == False


class TestOpDir(unittest.TestCase):
    def setUp(self):
        with open('test_example1.txt', 'w') as f:
            f.write('hello world')
        with open('test_example2.txt', 'w') as f:
            f.write('i am a tester')

    def test_list_dir_info_normal(self):
        files = list_dir_info("..")
        self.assertEqual(len(files), 2)

    def test_list_dir_info_err(self):
        files = list_dir_info("..")
        self.assertNotEqual(len(files), 3)

    def tearDown(self):
        os.remove('test_example1.txt')
        os.remove('test_example2.txt')



if __name__ == '__main__':
    unittest.main()


shutil.copytree('script','same_script')
