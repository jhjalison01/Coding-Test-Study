import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

def bfs(q,blank):
  visited=[[-1]*n for _ in range(n)]
  for i,j in q:
    visited[i][j]=0
  
  time=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n:
        #빈 칸을 만났을 경우
        if graph[nx][ny]==0 and visited[nx][ny]==-1:
          q.append([nx,ny])
          visited[nx][ny]=visited[x][y]+1
          blank-=1
          time = max(time, visited[x][y] + 1)
        #비활성화 바이러스를 만났을 경우
        if graph[nx][ny]==2 and visited[nx][ny]==-1:
          q.append([nx,ny])
          visited[nx][ny]=visited[x][y]+1
  if blank==0:
    return time
  else:
    return INF

n,m=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
INF=int(1e9)

graph=[]
virus_loc=[]
blank=0
for i in range(n):
  row = list(map(int,input().split()))
  for j in range(n):
    if row[j]==2:
      virus_loc.append([i,j])
    elif row[j]==0:
      blank+=1
  graph.append(row)

answer=INF
#활성화 바이러스 조합 구하기
for combination in combinations(virus_loc,m):
  q=deque(list(combination))
  
  #bfs 실행
  answer = min(answer, bfs(q, blank))

if answer != INF:
  print(answer) #최소 시간 출력
else:
  print(-1) #모든 빈칸에 바이러스를 퍼뜨릴 수 없는 경우