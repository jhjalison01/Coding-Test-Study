import sys
input=sys.stdin.readline

INF = int(1e9)
n,m=map(int,input().split())

#2차원 리스트로 만들고 무한으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]
#간선에 대한 정보 입력 받기
for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

#자기 자신에서 자기 자신으로 가는 것은 0으로 초기화
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0

#플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b], graph[a][k] + graph[k][b])

#2개의 건물을 선택하여 모든 도시를 방문하는데에 걸리는 거리를 측정
min_sum=INF
result=list()
for i in range(1,n+1):
  for j in range(1,n+1):
    distance=0
    #모든 건물을 방문
    for k in range(1,n+1):
      # i,j 번째 건물 중 가까운 거리의 2배 더함
      distance+=min(graph[k][i],graph[k][j])*2

    if distance<min_sum:
      min_sum=distance
      result=[i,j,min_sum]

#건물 번호, 모든 도시에서의 왕복 시간의 합
print(*result)