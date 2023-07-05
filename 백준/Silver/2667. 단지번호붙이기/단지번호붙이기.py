from collections import deque

#지도의 크기 입력 받기
n=int(input())
#지도 정보 입력 받기
graph=[[] for _ in range(n)]
for i in range(n):
  data=input()
  for j in range(n):
    graph[i].append(int(data[j]))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

#BFS 구현
def bfs(x,y):
  q=deque()
  q.append((x,y))
  result=1 #단지내 집의 수
  graph[x][y]=2
  #큐가 빌 때까지 반복
  while q:
    x,y=q.popleft()
    for i in range(4): #현재 위치에서 상하좌우 확인
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
        result+=1
        q.append((nx,ny))
        graph[nx][ny]=2 #탐색한 곳은 2로 표시
  return result

answer=0 #총 단지수
houses=[]#각 단지내 집의 수

for i in range(n):
  for j in range(n):
    if graph[i][j]==1: #값이 1인 곳 탐색
      house=bfs(i,j) #집의 수
      answer+=1
      houses.append(house)

#총 단지수 출력
print(answer)
#각 단지내 집의 수를 오름차순으로 정렬, 출력
houses.sort()
for x in houses:
  print(x)