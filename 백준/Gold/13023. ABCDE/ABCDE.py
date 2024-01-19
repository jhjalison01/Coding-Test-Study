import sys
input=sys.stdin.readline

n,m=map(int,input().split())

#그래프 정보 입력
graph=[[] for _ in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

finished=False
visited=[False]*(n+1)

#dfs 실행
def dfs(now, depth):
  global finished
  visited[now]=True
  if depth==4:
    finished=True
    return
  for i in graph[now]:
    if not visited[i]:
      dfs(i,depth+1)
      visited[i]=False

for i in range(n):
  dfs(i,0)
  visited[i]=False
  if finished:
    break

if finished: #조건에 맞는 a,b,c,d,e,가 존재할 경우
  print(1)
else:
  print(0)