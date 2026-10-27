"""重复文件清理器
    '设置空字典'
    '先打出文件'
    '遍历文件名'
    '设置限制文件重命名的条件，两个文件相同字母出现相似度不能大于4个字母，文件总名长度为8个字母'
    '出现疑似同名就全部打印同名文件'
    '文件大小相同一样打印出来'
"""



"""重复文件清理器"""
import os

def file_cleanup(folder_path):
    # 设置空字典
    file_info = {}
    duplicate_list = []

    # 遍历文件夹内所有文件
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            stat = os.stat(full_path)
            file_size = stat.st_size
            name_no_ext = os.path.splitext(filename)[0]  # 去掉后缀

            file_info[filename] = {
                "path": full_path,
                "size": file_size,
                "name": name_no_ext
            }

    # 比对逻辑：文件名相似度 + 文件大小
    all_files = list(file_info.values())
    for i in range(len(all_files)):
        for j in range(i+1, len(all_files)):
            f1 = all_files[i]
            f2 = all_files[j]

            # 条件1：文件名总长度为6个字母
            if len(f1["name"]) == 8 and len(f2["name"]) == 8:
                # 计算相同位置字符数量
                same_char = sum(c1 == c2 for c1, c2 in zip(f1["name"], f2["name"]))
                # 相同字母大于4个，判定疑似同名
                if same_char > 4:
                    duplicate_list.append((f1["path"], f2["path"]))
                    print(f"疑似同名文件：{f1['path']} 和 {f2['path']}")

            # 条件2：文件大小相同，判定重复
            if f1["size"] == f2["size"]:
                duplicate_list.append((f1["path"], f2["path"]))
                print(f"文件大小相同：{f1['path']} 和 {f2['path']}")

    # 统计所有重复文件个数（去重）
    dup_files = set()
    for a,b in duplicate_list:
        dup_files.add(a)
        dup_files.add(b)
    return len(dup_files)



