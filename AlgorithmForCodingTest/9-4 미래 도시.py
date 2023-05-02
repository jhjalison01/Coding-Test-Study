#이것이 취업을 위한 코딩 테스트다 Chapter 9 최단 경로 실전문제 2 <미래 도시>
n, m = map(int, input().split()) #노드, 간선 개수 입력 받기
INF=int(1e9) #무한 값 설정
graph=[[INF]*(n+1) for _ in range(n+1)] # 2차원 리스트로 그래프 구현

for i in range(n+1): #자기 자신에서 자기 자신으로 가는 시간을 0으로 설정
  graph[i][i]=0

for i in range(m):
  x,y=map(int, input().split())
  #x에서 y로 가는 시간을 각각 1로 설정
  graph[x][y]=1
  graph[y][x]=1

x, k = map(int, input().split()) #거쳐 갈 노드 x와 최종 목적지 노드 k를 입력 받기

#플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

if graph[1][k]==INF or graph[k][x]==INF: # 도달할 수 없으면 1을 출력
  print(-1)
else:
  print(graph[1][k]+graph[k][x]) #도달할 수 있다면 최소 이동 시간 출력
