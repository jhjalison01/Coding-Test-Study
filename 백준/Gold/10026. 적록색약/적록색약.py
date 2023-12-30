import sys
input=sys.stdin.readline
from collections import deque

n=int(input())

graph=[list(input().rstrip()) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  visited[x][y]=True
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[x][y]==graph[nx][ny]:
        q.append((nx,ny))
        visited[nx][ny]=True

visited=[[False]*n for _ in range(n)]
cnt1=0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt1+=1

#적록색약일 경우
for i in range(n):
  for j in range(n):
    if graph[i][j]=='R':
      graph[i][j]='G'

cnt2=0
visited=[[False]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i,j)
      cnt2+=1

print(cnt1, cnt2)