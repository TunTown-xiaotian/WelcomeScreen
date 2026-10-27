import os
import shutil
from pathlib import Path

# 把当前工作目录，切换到 area.py 所在的 src 文件夹
os.chdir(os.path.dirname(__file__))
print(__file__)
base = Path(__file__).parent
# 下面全部是相对路径！
src_file = "dir_path.txt"
dst_file = "tem/dir_path.txt"
shutil.move(os.path.join(base,src_file), os.path.join(base,dst_file))

