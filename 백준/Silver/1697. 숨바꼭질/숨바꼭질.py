import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
MAX=100000
dist=[0]*(MAX+1)

#bfs 이용
q=deque()
q.append(n)

while q:
  x=q.popleft()
  #k에 도착한 경우
  if x==k:
    print(dist[x])
    break
  #3가지 경우 확인
  for nx in (x+1,x-1,x*2):
    if 0<=nx<=MAX:
      #아직 최소거리를 구하지 않은 경우
      if dist[nx]==0:
        dist[nx]=dist[x]+1
        q.append(nx)