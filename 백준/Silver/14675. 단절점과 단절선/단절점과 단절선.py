import sys
input=sys.stdin.readline

n=int(input())

graph=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


q=int(input())
for _ in range(q):
  t,k=map(int,input().split())
  if t==1: #k번 정점이 단절점인지
    if len(graph[k])<2:
      print("no")
    else:
      print("yes")
  else: #k번 정점이 단절선인지
    #모든 간선은 노드 2개를 연결하고 있기 때문에 항상 yes
    print("yes")