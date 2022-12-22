import sys

def push(list, num):
    list.append(num)

def pop(list):
    if len(list)==0:
        return -1
    else:
        return list.pop()

def size(list):
    return len(list)

def empty(list):
    if len(list)==0:
        return 1
    else:
        return 0

def top(list):
    if len(list)==0:
        return -1
    else:
        return list[len(list)-1]

n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a=sys.stdin.readline()
    if a.startswith('push'):
        com, num=a.split()
        num=int(num)
        push(li,num)
    elif a.startswith('pop'):
        print(pop(li))
    elif a.startswith('size'):
        print(size(li))
    elif a.startswith('empty'):
        print(empty(li))
    elif a.startswith('top'):
        print(top(li))