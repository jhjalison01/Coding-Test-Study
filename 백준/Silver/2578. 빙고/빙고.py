import sys
input=sys.stdin.readline

board = []
for _ in range(5):
  row = list(map(int,input().split()))
  board.append(row)

nums = []
for _ in range(5):
  nums += list(map(int, input().split()))

def check():
  bingo = 0
  #가로 확인
  for row in board:
    if row.count(0) == 5:
      bingo += 1
      
  #세로 확인
  for i in range(5):
    y=0
    for j in range(5):
      if board[j][i] == 0:
        y+=1
    if y == 5:
      bingo+=1
      
  #왼쪽 위부터 시작하는 대각선 확인
  cnt1=0
  for i in range(5):
    if board[i][i] == 0:
      cnt1+=1
  if cnt1 == 5:
    bingo+=1
    
  #오른쪽 위부터 시작하는 대각선 확인
  cnt2 = 0
  for i in range(5):
    if board[i][4-i] == 0:
      cnt2+=1
  if cnt2 == 5:
    bingo+=1
  return bingo

cnt=0
for i in range(25):
  for x in range(5):
    for y in range(5):
      if nums[i] == board[x][y]:
        board[x][y]=0
        cnt+=1
  if cnt>=12:
    result=check()
    if result >=3:
      print(i+1)
      break