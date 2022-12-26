import sys
from collections import deque

n=int(sys.stdin.readline())
list = deque()

for _ in range(n):
    command=sys.stdin.readline().strip().split(' ')
    if command[0]=='push_front':
        list.appendleft(command[1])
    elif command[0]=='push_back':
        list.append(command[1])
    elif command[0]=='pop_front':
        if len(list)==0:
            print(-1)
        else:
            print(list.popleft())
    elif command[0]=='pop_back':
        if len(list)==0:
            print(-1)
        else:
            print(list.pop())
    elif command[0]=='size':
        print(len(list))
    elif command[0]=='empty':
        if len(list)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if len(list)==0:
            print(-1)
        else:
            print(list[0])
    elif command[0]=='back':
        if len(list)==0:
            print(-1)
        else:
            print(list[len(list)-1])