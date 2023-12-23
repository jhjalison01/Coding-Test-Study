import sys
input=sys.stdin.readline

def dfs(v, cnt):
  visited[v]=1
  #v와 연결된 노드 확인
  for i in graph[v]:
    #i에 아직 가지 않은 경우
    if visited[i]==0:
      #cnt 증가하고 dfs 실행
      cnt=dfs(i,cnt+1)
  return cnt

case=int(input())
for _ in range(case):
  n,m=map(int,input().split())
  #그래프 정보 입력 받기
  graph=[[] for _ in range(n+1)]
  for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

  visited=[0]*(n+1)
  answer=dfs(1,0)
  print(answer)