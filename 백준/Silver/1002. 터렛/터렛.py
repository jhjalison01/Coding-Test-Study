import sys
input=sys.stdin.readline
import math

T=int(input())

for _ in range(T):
  x1,y1,r1,x2,y2,r2=map(int,input().split())

  #두 원의 중심 사이 거리 구하기
  dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
  
  #두 원의 중심이 같을 경우
  if dis==0:
    if r1==r2: #두 원의 크기 같아 겹치는 경우
      print(-1)
    else: #두 원의 크기 같아 만나지 않는 경우
      print(0)
  else: #두 원의 중심이 다를 경우
    #두 원이 접하는 경우
    if dis==r1+r2 or abs(r1-r2)==dis:
      print(1)
    #두 원이 2점에서 만나는 경우
    elif (r1+r2)>dis and abs(r1-r2)<dis:
      print(2)
    else: #두 원이 만나지 않는 경
      print(0)