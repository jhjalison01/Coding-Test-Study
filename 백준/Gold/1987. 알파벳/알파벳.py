import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# n: 세로, m:가로
n,m=map(int,input().split())
#board: 보드
board=[]
for i in range(n):
  board.append(list(input().rstrip()))
#max_cnt: 말이 지날 수 있는 최대의 칸 수
max_cnt=1

path=set(board[0][0])

def dfs(x,y,cnt):
  global max_cnt
  #최대 칸 수 업데이트
  max_cnt=max(max_cnt, cnt)
  
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      #지나온 칸에 해당 알파벳이 없을 때
      if board[nx][ny] not in path:
        path.add(board[nx][ny])
        dfs(nx,ny,cnt+1)
        path.remove(board[nx][ny])

dfs(0,0,1)

#말이 지날 수 있는 최대 칸 수 출력
print(max_cnt)