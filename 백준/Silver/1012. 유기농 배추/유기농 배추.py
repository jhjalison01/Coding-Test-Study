from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

#bfs 구현
def bfs(x,y):
  q=deque()
  q.append((x,y))
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #범위 내에 있고 아직 확인하지 않았을 경우
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
        graph[nx][ny]=2 #확인한 배추는 2로 표시
        q.append((nx,ny)) #큐에 추가
    
#테스트 케이스 개수
t=int(input())

#테스트 케이스 만큼 반복
for x in range(t):
  #배추밭 가로, 세로, 배추 개수
  m,n,k=map(int,input().split())
  #배추밭의 정보 입력
  graph=[[0 for j in range(m)] for i in range(n)]
  for i in range(k):
    y,x=map(int,input().split())
    graph[x][y]=1

  result=0 #배추흰지렁이 개수
  #모든 배추 확인
  for i in range(n):
    for j in range(m):
      if graph[i][j]==1: #아직 확인하지 않은 배추에 bfs 탐색 실행
        bfs(i,j)
        result+=1
  print(result)