def push(list, num):
    list.append(num)

def pop(list):
    if len(list)==0:
        return -1
    else:
        return list.pop(0)

def size(list):
    return len(list)

def empty(list):
    if len(list)==0:
        return 1
    else:
        return 0

def front(list):
    if len(list)==0:
        return -1
    else:
        return list[0]

def back(list):
    if len(list)==0:
        return -1
    else:
        return list[len(list)-1]

import sys

n=int(sys.stdin.readline())
list=[]

for _ in range(n):
    command=sys.stdin.readline().split()
    if command[0]=='push':
        push(list,int(command[1]))
    elif command[0]=='pop':
        print(pop(list))
    elif command[0]=='size':
        print(size(list))
    elif command[0]=='empty':
        print(empty(list))
    elif command[0]=='front':
        print(front(list))
    elif command[0]=='back':
        print(back(list))