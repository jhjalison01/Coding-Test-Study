#이것이 취업을 위한 코딩 테스트다 Part3 DFS/BFS 16. 연구소
import sys
input=sys.stdin.readline

n,m=map(int, input().split())

#지도 입력 받기
graph=[] 
for i in range(n):
  graph.append(list(map(int, input().split())))

#벽을 세운 임시 지도
temp=[[0]*m for _ in range(n)]

result=0

#상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#dfs 이용하여 임시 지도에 바이러스를 퍼지게 하기
def virus(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx and nx<n and 0<=ny and ny<m:
      if temp[nx][ny]==0:
        temp[nx][ny]=2
        virus(nx,ny)

#안전 영역 크기 구하기
def get_score():
  score=0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        score+=1
  return score

#dfs 이용하여 벽을 세우면서 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  #3개의 벽을 다 설치했을 경우
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j]=graph[i][j]
    # 각 바이러스 퍼뜨리기
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    # 안전 영역 최댓값 계산
    result=max(result,get_score())
    return
  #빈 공간 벽 세우기
  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        graph[i][j]=1
        count+=1
        dfs(count)
        graph[i][j]=0
        count-=1

dfs(0)
print(result)
