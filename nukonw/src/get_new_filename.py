import os
import shutil
from  pathlib import Path

def batch_rename_files(dir_name="images"):
    base = Path(__file__).parent
    base_dir = os.path.join(base,dir_name)
    print(base_dir)

    count = 0
    for index, file in enumerate(os.listdir(base_dir),start=1):
        file_path = os.path.join(base_dir,file)
        if os.path.isfile(file_path):
            dest_file_path = os.path.join(base_dir,f"旅行_{index}.jpg")
            os.rename(file_path, dest_file_path)
            count += 1
    return count



def backup_dir(src,dst):
    base = Path(__file__).parent
    back_come = os.path.join(base, '')
    if os.path.exists(dst):
        os.rename(dst,back_come)
    shutil.copytree(src,dst)



if __name__ == "__main__":
    print(batch_rename_files())