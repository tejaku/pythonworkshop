"'welcome to python'"
def sample():
    print('welcome to module')
    
def add(*a):
    s=0
    for i in a:
        s+=i
    return s

def sub(a,b):
    return a-b
def multiply(*c):
    s=1
    for i in c:
        s*=i
    return s
def division(a,b):
    return a/b