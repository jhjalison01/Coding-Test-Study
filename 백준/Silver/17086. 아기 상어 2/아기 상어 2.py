import sys
input=sys.stdin.readline
from collections import deque

#n:세로 길이, m:가로 길이
n,m=map(int,input().split())

q=deque()
#board: 공간
board=[]
for i in range(n):
  temp=list(map(int,input().split()))
  board.append(temp)
  for j in range(m): #큐에 아기 상어가 있는 좌표 넣기
    if temp[j]==1:
      q.append((i,j))

#상하좌우, 대각선
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,1,-1,1,-1]

def bfs():
  while q:
    x,y=q.popleft()
    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
        q.append((nx,ny))
        board[nx][ny]=board[x][y]+1
        
bfs()
answer=0
for i in range(n):
  for j in range(m):
    answer=max(answer,board[i][j])

#안전 거리의 최댓값 출력
print(answer-1)