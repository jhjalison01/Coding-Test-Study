from collections import deque
import sys
input = sys.stdin.readline

n,l,r=map(int,input().split())
answer=0

#전체 나라의 정보 입력 받기
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

#이동할 네 방향 정의(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def bfs(x,y,index):
  united=[] #연합된 국가들 저장
  united.append((x,y))
  
  q=deque()
  q.append((x,y))
  union[x][y]=index #현재 연합 번호 할당
  people=data[x][y] #연합 국가 총 인구수
  count=1 #연합 국가의 수
  while q:
    x,y=q.popleft()
    #현재의 위치에서 상하좌우 확인
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #상하좌우에 있는 나라와 인구 비교
      if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
        #옆에 있는 나라와 인구 차이가 L명 이상, R명 이하 일 때
        if l<=abs(data[nx][ny]-data[x][y])<=r:
          q.append((nx,ny))
          #연합에 추가
          union[nx][ny]=index
          people+=data[nx][ny]
          count+=1
          united.append((nx,ny))
  #연합 국가끼리 인구 분배
  for i,j in united:
    data[i][j]=people//count
    
#더 이상 인구이동을 할 수 없을 때까지 반복
while True:
  union=[[-1]*n for _ in range(n)]
  index=0
  for i in range(n):
    for j in range(n):
      if union[i][j]==-1: #해당 나라가 아직 처리되지 않았을 경우
        bfs(i,j,index)
        index+=1
  #모든 인구 이동이 끝난 경우
  if index==n*n:
    break
  answer+=1
  
print(answer)
  
