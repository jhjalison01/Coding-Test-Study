from itertools import combinations
import sys
input = sys.stdin.readline

n=int(input())
data=[]
teachers=[]
spaces=[]

for i in range(n):
  #복도 정보 입력 받기
  data.append(list(input().split()))
  for j in range(n):
    if data[i][j]=='T':
      teachers.append((i,j)) #선생님 위치 정보
    if data[i][j]=='X':
      spaces.append((i,j)) #빈 공간 위치 정보
    

#한 방향에 학생이 있는지 확인
def watch(x,y,direction):
  #왼쪽 방향 확인
  if direction==0:
    while y>=0:
      if data[x][y]=='S':
        return True
      if data[x][y]=='O':
        return False
      y-=1
  #오른쪽 방향 확인
  if direction==1:
    while y<n:
      if data[x][y]=='S':
        return True
      if data[x][y]=='O':
        return False
      y+=1
  #위쪽 방향 확인
  if direction==2:
    while x>=0:
      if data[x][y]=='S':
        return True
      if data[x][y]=='O':
        return False
      x-=1
  #아래쪽 방향 확인
  if direction==3:
    while x<n:
      if data[x][y]=='S':
        return True
      if data[x][y]=='O':
        return False
      x+=1
  return False

#상하좌우에 학생이 한 명이라 있는지 확인
def process():
  for x,y in teachers:
    for i in range(4):
      if watch(x,y,i):
        return True
  return False

find=False #학생들이 감시를 다 피할 수 있는지의 여부

#빈 공간에 3개의 장애물을 뽑는 모든 조합 확인
for obstacles in combinations(spaces,3):
  #빈 공간에 장애물 설치
  for x,y in obstacles:
    data[x][y]='O'
  # 학생이 한 명도 감지되지 않은 경우
  if not process():
    find=True
    break
  #학생이 한 명이라도 감지됐을 경우 설치한 장애물 제거
  for x,y in obstacles:
    data[x][y]='X'

if find:
  print("YES")
else:
  print("NO")
