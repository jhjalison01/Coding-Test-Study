#이것이 취업을 위한 코딩 테스트다 Part3 구현 11. 뱀
#뱀은 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남
#처음 뱀은 맨 위 맨 좌측에 위치, 오른쪽을 보고 있음

n=int(input()) #보드의 크기 입력 받기
k=int(input()) # 사과의 개수 입력 받기
data=[[0]*(n+1) for i in range(n+1)] # 보드 구현
move=[]

#사과가 있은 곳은 1로 표시
for i in range(k):
  a,b=map(int, input().split())
  data[a][b]=1

#뱀의 방향 변환 횟수 입력 받기
l=int(input())

#뱀의 방향 변환 정보 입력 받기
for _ in range(l):
  a,b=input().split()
  move.append([int(a),b])

#동, 남, 서, 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction, c):
  if c=='L':
    direction=(direction-1)%4
  else:
    direction=(direction+1)%4
  return direction

def simultate():
  x,y=1,1 #뱀의 머리가 존재하는 곳
  data[x][y]=2 #뱀이 존재하는 위치는 2로 표시
  direction=0 #뱀 머리 방향, 처음에는 동쪽을 보고 있음
  time=0 #시작한 뒤 지난 시간
  index=0 #다음에 회전할 정보
  q=[(x,y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽), 큐 사용

  while True:
    nx=x+dx[direction]
    ny=y+dy[direction]
    #맵 범위 안에 있고 뱀의 몸통이 없는 위치일 경우
    if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny]!=2:
      #해당 위치에 사과가 없을 때 꼬리 제거
      if data[nx][ny]==0:
        data[nx][ny]=2
        q.append((nx,ny))
        px,py=q.pop(0)
        data[px][py]=0
      #사과가 있다면 이동 후 꼬리 그대로 두기
      if data[nx][ny]==1:
        data[nx][ny]=2
        q.append((nx,ny))
    else:#벽이나 몸통에 부딪혔을 때
      time+=1
      break
    x,y=nx,ny
    time+=1
    if index<len(move) and time==move[index][0]: #회전할 시간이 됐으면 회전
      direction=turn(direction,move[index][1])
      index+=1
  return time

print(simultate())