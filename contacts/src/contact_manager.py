import os.path

FILENAME = "contacts.txt"

def load_contacts():
    """从文件加载通讯录，返回 {姓名: 电话} 字典"""
    contacts = {}
    """用来存储名字和电话"""
    try:#用try来捕获抛出异常的代码
        with open(FILENAME, "r", encoding="utf-8") as f:
            """用with可以自动关闭文件，open打开文件，r只能读取文件内容，不能修改"""
            for line in f:
                """遍历f文件的没一行代码，防止内存爆炸💥"""
                line = line.strip()
                """删除没一行的空格并赋值给每一行"""
                if not line:
                    """如果没有这一行，那就返回继续"""
                    continue
                name, phone = line.split(",")
                """用split拆分没一行，形成name和phone"""
                contacts[name] = phone
                """把该文件的键name和值phone存到contacts"""
    except FileNotFoundError:
        pass  # 第一次运行，文件还不存在
    return contacts

def save_contacts(contacts):
    """把通讯录整体写回文件"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")

def save_contacts_append(name, phone):
     with open(FILENAME, "a", encoding="utf-8") as f:
         f.write(f"{name},{phone}\n")

def add_contact(contacts):
    name = input("姓名：").strip()
    phone = input("电话：").strip()
    if name in contacts:
        print("该联系人已存在！")
        return
    contacts[name] = phone
    # save_contacts(contacts)
    save_contacts_append(name,phone)
    print("添加成功！")
def delete_contact(contacts):
    name=input('请输入你想要删除的联系人： ').strip()
    if name not in contacts:
        print('该联系人不存在')
        return
    del contacts[name]
    save_contacts(contacts)
    print(f'联系人{name}删除成功')
def amend_contact(contacts):
    name=input('选择你要修改的联系人：')
    if name not in contacts:
        print('你要修改的联系人不存在')
        return
    new_phone=input('请输入你要修改的电话:  ').strip()
    contacts[name]=new_phone
    save_contacts(contacts)
    print("修改成功！")
def show_contacts(contacts):
    if not contacts:
        print("通讯录为空。")
        return
    for name, phone in contacts.items():
        print(f"{name}：{phone}")

def main():
    contacts = load_contacts()
    while True:
        print("\n===== 通讯录 =====")
        print("1. 查看  2. 添加  3.删除 4.修改 0. 退出")
        choice = input("请选择：")
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            amend_contact(contacts)
        elif choice == "0":
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()