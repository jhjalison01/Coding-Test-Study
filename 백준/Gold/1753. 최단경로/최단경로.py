import sys
input=sys.stdin.readline
import heapq
INF=int(1e9)

v,e=map(int,input().split()) # 정점 개수, 간선 개수
start=int(input())  #시작 정점
graph=[[] for i in range(v+1)]
distance=[INF]*(v+1) #최단 거리 테이블을 모두 무한으로 초기화

#간선 정보 입력받기
for i in range(e):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

#다익스트라 알고리즘 구현
def sol(start):
  q=[]
  #시작 노드의 최단 거리를 0으로 설정, 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: #큐가 빌 때까지 반복
    dist, now = heapq.heappop(q)
    #현재 노드가 이미 처리된 적이 있는 경우 무시
    if distance[now]<dist:
      continue
    #현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]:
      cost=dist+i[1]
      #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

sol(start)

for i in range(1,v+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])