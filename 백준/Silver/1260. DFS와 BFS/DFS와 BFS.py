from collections import deque

n, m,v = map(int, input().split())

#그래프를 리스트 자료형으로 표현
graph=[]
for i in range(1001):
  graph.append([])

#각 노드가 연결된 정보를 표현
for i in range(m):
  a, b =map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

#각 노드가 방문된 정보를 리스트 자료형으로 표현
visited=[False]*1001
visited_bfs=[False]*1001

#dfs 메소드 정의
def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v]=True
  print(v, end=' ')
  #번호가 작은 노드부터 먼저 방문하기 위해 숫자 정렬
  graph[v].sort()
  #현재 노드와 연결된 노드 중 방문한 적이 없는 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i, visited)

#bfs 메소드 정의
def bfs(graph, v, visited):
  #큐 구현을 위해 deque 라이브러리 이용
  queue=deque([v])
  #현재 노드를 방문 처리
  visited[v]=True
  #큐가 빌 때까지 반복한다
  while queue:
    #큐에서 하나의 원소를 뽑아 출력한다
    v=queue.popleft()
    print(v, end=' ')
    #번호가 작은 노드부터 먼저 방문하기 위해 숫자 정렬
    graph[v].sort()
    #현재 노드에 연결된 노드 중 방문한 적이 없는 노드를 큐에 삽입&방문 처리
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True
  

dfs(graph, v, visited)
print()
bfs(graph, v, visited_bfs)