from collections import deque
import sys

n,m=map(int, sys.stdin.readline().split())

graph=[]

#그래프를 리스트 자료형으로 표현
for i in range(n+1):
  graph.append([])

#각 노드가 연결된 정보를 표현
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

#각 노드가 방문된 정보를 리스트 자료형으로 표현
visited=[False]*(n+1)

#bfs 메소드 정의
def bfs(v):
  queue=deque([v])
  visited[v]=True
  while queue:
    v=queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

answer=0

#연결 요소 세기
for i in range(1,n+1):
  if not visited[i]:
    #bfs를 한 번 실행하면 하나의 노드의 연결 요소들이 모두 방문 처리된다.
    bfs(i)
    answer+=1

print(answer)