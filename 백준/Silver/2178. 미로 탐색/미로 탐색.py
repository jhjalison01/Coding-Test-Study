from collections import deque
#NxM 크기 입력 받기
n,m=map(int,input().split())
#미로 정보 입력 받기
graph=[[] for _ in range(n)]
for i in range(n):
  data=input()
  for j in range(m):
    graph[i].append(int(data[j]))

#상하좌우
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

#bfs 구현
def bfs(x,y):
  q=deque() #큐 사용
  q.append((x,y))
  while q:
    x,y=q.popleft()
    #상하좌우 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #범위에서 벗어나지 않고 값이 1일 경우
      if 0<=nx and nx<n and 0<=ny and ny<m and graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1 #1 더한 값을 graph[nx][ny]에 저장
        q.append((nx,ny)) #큐에 추가
  return graph[n-1][m-1] #(n,m) 값 반환

print(bfs(0,0))