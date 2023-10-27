import sys
input=sys.stdin.readline
  
N=int(input())

graph=[]
for _ in range(N):
  graph.append(list(map(int,input().split())))

#좌하우상
dx=[0,1,0,-1]
dy=[-1,0,1,0]

#방향별 모래 비율
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
   (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

#토네이도 처음 위치
r,c=N//2,N//2
direc=0
answer=0
dict = {0: left, 1: down, 2: right, 3: up}
time = 0

def solve(x,y,direc):
  global answer
  if x<0 or y<0:
    return
    
  total=0
  for dx,dy,z in direc:
    nx=x+dx
    ny=y+dy
    if z==0: #a일 경우
      new_sand=graph[x][y]-total
    else: #비율일 경우
      new_sand = int(graph[x][y]*z)
      total += new_sand
    if 0 <= nx < N and 0 <= ny < N:  # 범위에 포함될 경우 값 갱신
      graph[nx][ny] += new_sand
    else:  # 범위 밖이면 ans 카운트
      answer += new_sand

for i in range(2*N-1):
  d=i%4
  if d==0 or d==2:
    time+=1
  for _ in range(time):
    nx=r+dx[d]
    ny=c+dy[d]
    solve(nx,ny,dict[d])
    r,c=nx,ny

print(answer)