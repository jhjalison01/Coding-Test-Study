import sys
input=sys.stdin.readline
from collections import deque
#스카이 콩콩의 힘, 동규의 현재위치, 주미의 현재위치
a,b,n,m=map(int,input().split())
        
graph=[0 for _ in range(100001)]
visited=[False for _ in range(100001)]
#-1,+1,+a,-a,+b,-b, a배, b배
dx=[-1,1,a,-a,b,-b,a,b]

def bfs(a):
  q=deque([a])
  visited[a]=True

  while q:
    x=q.popleft()

    for i in range(8):
      #6가지 경우는 덧셈 연산
      if i<6:
        nx=x+dx[i]
      else:
        #나머지는 곱셈 연산
        nx=x*dx[i]
      #범위 내에 있고 탐색하지 않은 경우
      if 0<=nx<=100000 and not visited[nx]:
        q.append(nx)
        visited[nx]=True
        graph[nx]=graph[x]+1
        
        
bfs(n)
print(graph[m])