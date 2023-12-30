import sys
input=sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))

check=[0 for _ in range(n)]

def dfs(x):
  for i in range(n):
    #x에서 i로 가는 길이 있고 i로 가지 않은 경우
    if graph[x][i]==1 and check[i]==0:
      check[i]=1
      #dfs 실행
      dfs(i)

for i in range(n):
  dfs(i)
  print(*check)
  check=[0 for _ in range(n)]