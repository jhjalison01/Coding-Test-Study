import copy
import sys
input=sys.stdin.readline
#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

mode=[
  [],
  [[0],[1],[2],[3]],
  [[0,1],[2,3]],
  [[0,3],[0,2],[1,3],[1,2]],
  [[1,2,3],[0,2,3],[0,1,3],[0,1,2]],
  [[0,1,2,3]]
]
#감시
def fill(data,mode,x,y):
    for i in mode: #방향에 따라
      nx=x
      ny=y
      while True:
        nx+=dx[i]
        ny+=dy[i]
        if 0<=nx<n and 0<=ny<m:
          if data[nx][ny]==6:
            break
          if data[nx][ny]==0:
            data[nx][ny]=-1
        else:
          break
    
def solve(data,depth):
  global answer
  #탐색을 다 했을 경우
  if depth==len(cameras):
    cnt=0
    #사각지대 개수 구하기
    for i in range(n):
      cnt+=data[i].count(0)
    #최솟값 업데이트
    answer=min(answer,cnt)
    return
  #임시 사무실 저장
  temp=copy.deepcopy(data)
  camera_num,x,y=cameras[depth] #탐색할 cctv
  for i in mode[camera_num]:
    fill(temp,i,x,y) #cctv 감시
    solve(temp,depth+1) #재귀호출
    temp=copy.deepcopy(data)#사무실 초기화
      
#사무실 세로, 가로 크기 입력받기
n,m=map(int,input().split())
#사무실 정보 입력 받기
data=[]
for _ in range(n):
  data.append(list(map(int,input().split())))

#cctv 정보 저장
cameras=[]
for i in range(n):
  for j in range(m):
    if 0<data[i][j]<6:
      cameras.append([data[i][j],i,j])

answer=65
solve(data,0)
print(answer)