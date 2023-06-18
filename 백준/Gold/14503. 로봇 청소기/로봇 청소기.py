#d: 0-북, 1-동,2-남,3-서
#0-청소 안됨, 1-벽
#바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
x,y,d=map(int,input().split())
data=[] #방

#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

answer=0

#방의 상태를 입력받기
for i in range(n):
  data.append(list(map(int,input().split())))

while True:
  #현재 칸이 청소되지 않은 경우
  if data[x][y]==0:
    data[x][y]=2 #청소된 칸은 2로 표현
    answer+=1
  direction=d
  no_blank=True
  for i in range(4):
    direction=(direction-1)%4 #반시계 방향으로 90도 돌림
    nx=x+dx[direction]
    ny=y+dy[direction]
    #바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 경우
    if data[nx][ny]==0:
      x=nx
      y=ny
      d=direction
      no_blank=False
      break
  #현재 칸 주변 4칸 중 청소되지 않은 칸이 없는 경우
  if no_blank:
    #바라보는 방향을 유지한 채로 한 칸 후진할 수 없는 경우
    if data[x+dx[(d+2)%4]][y+dy[(d+2)%4]]==1:
      break #작동을 멈춤
    #한 칸 후진할 수 있는 경우 후진함
    else:
      x=x+dx[(d+2)%4]
      y=y+dy[(d+2)%4]

print(answer)