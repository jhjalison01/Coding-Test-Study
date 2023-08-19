#규칙 - 추가되는 커브는 이전 세대의 정보를 뒤집어 방향에 1을 더해준다.
#2세대 - 0 1 2 1 --> 뒤집으면 1 2 1 0이 됨 --> 여기에 +1을 해주면 2 3 2 1이 됨
#결국 3세대 방향은 0 1 2 1 2 3 2 1이 

import sys
input = sys.stdin.readline
#드래곤 커브의 개수 N 입력받기
n=int(input())

#우상좌하
dx=[1,0,-1,0]
dy=[0,-1,0,1]
#그래프 초기화
graph=[[0] * 101 for i in range(101)]

for i in range(n):
  #드래곤 커브 정보 입력 받기
  x,y,d,g=map(int,input().split())
  graph[x][y]=1
  #커브 리스트 만들기
  curve=[d]
  for _ in range(g):
    tmp=[]
    for k in range(len(curve)):
      tmp.append((curve[-k-1]+1)%4)
    curve.extend(tmp)

  #드래곤 커브 만들기
  for j in curve:
    x+=dx[j]
    y+=dy[j]
    graph[x][y]=1

#네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형 개수 구하기
answer=0
for i in range(100):
  for j in range(100):
    if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
      answer+=1

print(answer)