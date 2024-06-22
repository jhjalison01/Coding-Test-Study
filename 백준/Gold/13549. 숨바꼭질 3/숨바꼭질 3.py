import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())

INF = 100001
time=[0]*(INF)

def bfs(x,y):
  q=deque()
  q.append(x)
  time[x] = 1 # 시작 위치를 방문한 것으로 표시하고 시간을 1로 설정

  while q:
    x=q.popleft()
    #수빈이가 동생이 있는 위치에 도달했을 경우
    if y==x:
      return time[x]-1 # 처음 시작 시간을 1로 설정했으므로 최종 시간에서 1을 빼줌
    #위치 이동
    for nx in (x-1,x+1,x*2):
      if 0<=nx<INF and time[nx]==0:
        if nx==x*2:
          time[nx]=time[x]
          q.appendleft(nx)
        else:
          time[nx]=time[x]+1
          q.append(nx)

print(bfs(n,k))