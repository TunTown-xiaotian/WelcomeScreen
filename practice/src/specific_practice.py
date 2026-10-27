def read_file(path):
    """读取文件内容，出错时返回 None"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError()
        print(f"错误：文件 {path} 不存在")
    except PermissionError:
        print(f"错误：没有权限读取 {path}")
    except UnicodeDecodeError:
        print(f"错误：{path} 编码不是 utf-8，请检查")
    return None

if __name__ == "__main__":
    content = read_file("poem.txt")
    if content is not None:
        print(content)
