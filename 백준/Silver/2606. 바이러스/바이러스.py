import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

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

#1번 컴퓨터는 제외해야 하므로 초기값을 -1로 설정한다.
result=-1

#dfs 메소드 정의
def dfs(graph,v,visited):
  visited[v]=True
  global result
  result+=1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
  

dfs(graph,1,visited)
print(result)