import sys
input=sys.stdin.readline
from collections import deque

a,b=map(int,input().split())
answer=-1
q=deque()
q.append((a,1))

while q:
  num,cnt=q.popleft()
  #b가 된 경우
  if num==b:
    answer=cnt
    break
  if num*2<=b:
    #2배 한 수 큐에 넣기
    q.append((num*2,cnt+1))
  if num*10+1<=b:
    #오른쪽에 1 추가한 수 큐에 넣기
    q.append((num*10+1,cnt+1))
print(answer)