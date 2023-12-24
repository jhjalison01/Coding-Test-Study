import sys
input=sys.stdin.readline
from collections import deque

m,n,k=map(int,input().split())

#모눈종이 초기화
graph=[[0]*(n) for _ in range(m)]
for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs 구현
def bfs(x,y):
  area=1
  q=deque()
  #큐에 첫 부분 위치 넣기
  q.append((x,y))
  graph[x][y]=2
  while q: #큐가 빌 때까지 반복
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
        graph[nx][ny]=2
        q.append((nx,ny))
        area+=1
  return area

cnt=0
area=[]
for i in range(m):
  for j in range(n):
    #아직 확인하지 않은 부분일 경우
    if graph[i][j]==0:
      area.append(bfs(i,j)) #bfs 실행, 영역 넓이 저장
      cnt+=1 #영역 개수 증가

print(cnt)
area.sort()
print(*area)