from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
#지도 정보 입력 받기
graph=[]
for i in range(n):
  graph.append(list(input()))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  q=deque() #큐 사용
  q.append((x,y))
  cnt=0
  visited=[[0]*m for _ in range(n)]
  visited[x][y]=1
  while q:
    x,y=q.popleft()
    #상하좌우 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #범위에서 벗어나지 않고 육지이고 아직 가지 않은 경우
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='L' and visited[nx][ny]==0:
        #이전 이동 경로에 1 추가
        visited[nx][ny]=visited[x][y]+1
        cnt=max(cnt,visited[nx][ny])
        q.append((nx,ny))
  return cnt-1

result=0
for i in range(n):
  for j in range(m):
    if graph[i][j]=='L':
      result=max(bfs(i,j),result)

print(result)