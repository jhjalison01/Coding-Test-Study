import sys
input=sys.stdin.readline

dice=[0,0,0,0,0,0]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

#주사위 굴리기 0 - 윗면, 5 - 바닥면
def turn(dir):
  a,b,c,d,e,f=dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
  if dir==1: #동쪽
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=d,b,a,f,e,c
  elif dir==2: #서쪽
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=c,b,f,a,e,d
  elif dir==3: #북쪽
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=e,a,c,d,f,b
  elif dir==4: #남쪽
    dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]=b,f,c,d,a,e

#n: 지도 세로, m: 지도 가로, x,y: 주사위 좌표, k: 명령 개수
n,m,x,y,k=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

#동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
command=list(map(int,input().split()))

for comm in command:
  x+=dx[comm-1]
  y+=dy[comm-1]
  #범위에서 벗어났을 경우 명령 무시
  if x<0 or x>=n or y<0 or y>=m:
    x-=dx[comm-1]
    y-=dy[comm-1]
    continue
  #주사위 굴리기
  turn(comm)
  #칸에 0이 적혀져 있을 경우
  if graph[x][y]==0:
    graph[x][y]=dice[5]
  #칸에 0이 적혀져 있지 않을 경우
  else:
    dice[5]=graph[x][y]
    graph[x][y]=0
  #주사위의 윗 면에 쓰여 있는 수를 출력
  print(dice[0])