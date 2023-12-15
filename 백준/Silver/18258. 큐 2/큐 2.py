import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
q=deque()

for i in range(n):
  com=input().split()
  #큐에 넣기
  if com[0]=="push":
    q.append(com[1])
  #큐 앞에 정수 빼고 출력
  elif com[0]=="pop":
    if q:
      print(q.popleft())
    else:
      print(-1)
  #큐에 들어있는 정수 개수 출력
  elif com[0]=="size":
    print(len(q))
  #큐가 비어있는지 확인
  elif com[0]=="empty":
    if q:
      print(0)
    else:
      print(1)
  #큐 가장 앞에 있는 정수 출력
  elif com[0]=="front":
    if q:
      print(q[0])
    else:
      print(-1)
  #큐 가장 뒤에 있는 정수 출력
  elif com[0]=="back":
    if q:
      print(q[-1])
    else:
      print(-1)