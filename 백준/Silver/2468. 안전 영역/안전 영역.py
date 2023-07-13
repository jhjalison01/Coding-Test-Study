import copy
from collections import deque
#N 입력받기
n=int(input())
#지역 정보 입력받기
graph=[]
for i in range(n):
  graph.append(list(map(int, input().split())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs 구현
def bfs(x,y,value):
  q=deque()
  q.append((x,y))
  temp[x][y]=0 #방문 표시
  while q:
    x,y=q.popleft()
    for i in range(4): #상하좌우 확인
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and temp[nx][ny]>value and temp[nx][ny]!=0: #범위 내에 있고 값이 value보다 클 경우
        q.append((nx,ny)) #큐에 삽입
        temp[nx][ny]=0 #0으로 표시

max_value = max(map(max, graph)) #높이의 최댓값

if max_value==1:
  print(1)
else:
  answer=[]
  #1부터 높이의 최댓값까지 확인
  for k in range(1, max_value+1):
    
    temp=copy.deepcopy(graph) #2차원 배열이므로 deepcopy 사용
    result=0 #안전 영역의 개수
    for i in range(n):
      for j in range(n):
        if temp[i][j]>k and temp[i][j]!=0:
          bfs(i,j,k) #bfs 실행
          result+=1
    answer.append(result)
            
  print(max(answer))