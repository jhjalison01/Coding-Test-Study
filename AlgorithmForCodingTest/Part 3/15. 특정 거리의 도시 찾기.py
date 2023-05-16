#이것이 취업을 위한 코딩 테스트다 Part3 DFS/BFS 15. 특정 거리의 도시 찾기
from collections import deque

n,m,k,x=map(int,input().split())
#도로 정보 입력 받기
graph=[[] for i in range(n+1)]

for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)

#각 도시에 대한 최단 거리 초기화
distance=[-1]*(n+1)
distance[x]=0

#BFS 구현
q=deque([x])
while q:
  now=q.popleft()
  for next_node in graph[now]:
    if distance[next_node]==-1: #방문하지 않은 도시일 경우
      distance[next_node]=distance[now]+1 #최단 거리 입력
      q.append(next_node)#큐에 노드 넣기

check=False
for i in range(1,n+1): # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
  if distance[i]==k:
    print(i)
    check=True

if check==False: #최단 거리가 K인 도시가 없으면 -1 출력
  print(-1)
