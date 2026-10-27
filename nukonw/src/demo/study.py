from os import write
from random import choice
from re import split
import time
STUDY_DIARY="log.txt"
def load_study():
    study_diary=[]
    try:
        with open(STUDY_DIARY,'r',encoding='utf-8') as s:
            for line in s:
                line=line.strip()
                if not line:
                    continue
                time_str,content=line.split(',')
                study_diary.append((time_str,content))
    except FileNotFoundError:
        print('学习内容没有存储')
        return None
    return study_diary

def save_study(content):
    with open (STUDY_DIARY,'a',encoding='utf-8') as f:
        cur_time = time.strftime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write(f"{cur_time},{content}\n")

def append_content():
    content=input('输入学习内容: ').strip()
    save_study(content)
    print('学习内容添加成功')

def show_diary():
    content = load_study()
    if content is None:
        print(f"have no content now!")
        return
    for line_str in content:
        time_str,content_str = line_str[0],line_str[1]
        print(f"time: {time_str}\tcontent: {content_str}")

def main():
    study_diary=load_study()
    while True:
        print("\n===学习日志====")
        print('1.查看:  2.添加内容: 0. exit: ')
        choice=input('请选择: ')
        if choice=='1':
            show_diary()
        elif choice=='2':
            append_content()
        elif choice == '0':
            break
        else:
            print('无效选择')

if __name__=='__main__':
    main()
