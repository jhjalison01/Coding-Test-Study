import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())

hx,hy=map(int,input().split())
ex,ey=map(int,input().split())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))

#visited[x][y][magic]: (x,y) 지점에 남은 마법 횟수가 magic 일 경우 도달한 적이 있는지
visited=[[[False]*2 for _ in range(m)] for _ in range(n)]
visited[hx-1][hy-1][1]=True

def bfs():
  q=deque()
  q.append((hx-1,hy-1,1,0))
  
  while q:
    #magic: 남은 마법 횟수, cost: 걸린 시간
    x,y,magic,cost=q.popleft()
    if x==ex-1 and y==ey-1:
      return cost

    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if 0<=nx<n and 0<=ny<m and not visited[nx][ny][magic]:
        #(nx,ny)가 벽이고 마법을 쓸 수 있을 경우 - 마법 사용
        if magic==1 and graph[nx][ny]==1:
          visited[nx][ny][0]=True
          q.append((nx,ny,0,cost+1))
        #(nx,ny)가 빈 칸일 경우 - 그냥 이동
        elif graph[nx][ny]==0:
          visited[nx][ny][magic]=True
          q.append((nx,ny,magic,cost+1))
  return -1

print(bfs())