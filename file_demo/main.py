#file文件夹
#path路径
#os负责处理文件、文件夹、系统信息；如果只是读写文件open()，不用 os。
#os.listdir(文件夹)：列出文件夹里一级所有名字（文件 + 子文件夹）
#os.path.isfile(完整路径)：判断是不是文件
#os.path.isdir(完整路径)：判断是不是文件夹

# * 匹配任意字符，? 匹配单个字符
#glob.glob("*.txt")           # 当前目录所有 .txt 文件
#glob.glob("data/*.csv")      # data 目录下的 .csv
#glob.glob("**/*.py", recursive=True)  # 递归所有子目录找 .py




from pathlib import Path
import os

base = Path(__file__).parent
def duplicates_by_size(dir):
    size_map={}
    for root,_, files  in os.walk(dir):
        for filename in files:
            filepath = os.path.join(root,filename)
            try:
                file_size=os.path.getsize(filepath)
            except OSError:
                continue
            if file_size not in size_map:
                size_map[file_size] = []
            size_map[file_size].append(filepath)

    for size, path_list in size_map.items():
        if len(path_list) >= 2:
            print(f"=== 文件大小：{size} 字节 ===")
            for p in path_list:
                print(p)
            print()


if __name__ == "__main__":
    base = Path(__file__).parent
    duplicates_by_size(base)