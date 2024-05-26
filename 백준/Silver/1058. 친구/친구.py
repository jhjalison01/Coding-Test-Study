import sys
input=sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
  graph.append(input().rstrip())

# 2-친구 사이일 때 1, 아니면 0
friends = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      # 2-친구인 경우
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        friends[i][j] = 1

result=0
for row in friends:
  result = max(result, sum(row))
print(result)