import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

n=int(input())

#부모 노드 저장할 리스트
visited=[None for _ in range(n+1)]
#트리 정보 입력 받기
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)
#dfs 구현
def dfs(graph,vertex):
  for i in graph[vertex]:
    if not visited[i]:
      visited[i]=vertex #부모 노드 저장
      dfs(graph,i)

dfs(tree,1)

for i in range(2,n+1):
  print(visited[i])