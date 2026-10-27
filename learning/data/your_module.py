def add(a,b):
    return a*b


def your_function(x):
    items=[1,2,3,4,5]
    for x in items:
        if x%2==0:
            print(x)
        break


def factorial(n):
    if not isinstance(n,int):
        raise TypeError('输入必须是整数：')
    if n<0:
        raise ValueError('输入必须是正数：')
    if n in (0,1):
        return 1
    return n*factorial(n-1)

