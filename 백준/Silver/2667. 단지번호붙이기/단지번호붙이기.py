import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
graph=[]
for i in range(n):
  a=list(input().rstrip())
  graph.append(a)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  graph[x][y] = '2'
  q=deque()
  q.append((x,y))
  cnt=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and graph[nx][ny] == '1':
        graph[nx][ny]='2'
        cnt+=1
        q.append((nx,ny))
  return cnt

answer=[]
for i in range(n):
  for j in range(n):
    if graph[i][j] == '1':
      answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for num in answer:
  print(num)