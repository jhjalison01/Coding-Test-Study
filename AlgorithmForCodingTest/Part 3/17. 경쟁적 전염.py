#이것이 취업을 위한 코딩 테스트다 Part3 DFS/BFS 17. 경쟁적 전염
import sys
from collections import deque
input=sys.stdin.readline

#시험관 크기, 바이러스의 개수 입력 받기
n,k=map(int, input().split())

#시험관 정보 입력 받기
data=[]
virus=[]
for i in range(n):
  data.append(list(map(int, input().split())))
  #바이러스 위치 저장하기
  for j in range(n):
    if data[i][j]!=0:
      virus.append((data[i][j],0,i,j))

virus.sort()
q=deque(virus)

#s,x,y 입력 받기
target_s,target_x,target_y=map(int,input().split())

#상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs 실행
while q: #q가 비면 정지
  num,s,x,y=q.popleft()
  if s==target_s: #s초가 지나면 정지
    break
  for i in range(4): #상,하,좌,우 바이러스 퍼뜨리기
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx and nx<n and 0<=ny and ny<n:
      #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if data[nx][ny]==0:
        data[nx][ny]=num
        q.append((num,s+1,nx,ny))

print(data[target_x-1][target_y-1]) #(x,y)에 존재하는 바이러스 종류 출력
