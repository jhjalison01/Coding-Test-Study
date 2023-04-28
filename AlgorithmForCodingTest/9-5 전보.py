#이것이 취업을 위한 코 테스트다 Chapter 9 최단 거리 실전문제 3 <전보>
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

#노드의 개수, 간선의 개수, 시작 노드 입력 받기
n,m,c=map(int,input().split())
#각 노드에 연결되어 있는 노드 정보 받기
graph=[[] for i in range(n+1)]
#최단 거리 테이블 초기화
distance=[INF]*(n+1)

#간선 정보 입력받기
for _ in range(m):
  x,y,z=map(int, input().split())
  graph[x].append((y,z))

#다익스트라 알고리즘 구현
def dijkstra(start):
  q=[]
  #시작 노드의 최단 거리를 0으로 설정하여 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q: #큐가 빌 때까지 반복
    #최단 거리가 가장 짧은 노드 꺼내기
    dist, now = heapq.heappop(q)
    #현재 노드가 이미 처리된 노드라면 무시
    if distance[now]<dist:
      continue
    #현재 노드에 연결된 노드들을 확인
    for i in graph[now]:
      cost=dist+i[1]
      #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count=0 #메세지를 받는 도시의 총 개수
max_distance=0 #메세지를 받는데 걸리는 총 시간

for i in distance:
  if i!=INF:
    count+=1
    max_distance=max(max_distance,i)
    
print(count-1,max_distance) #시작 노드는 제외해야 하므로 count-1을 출력
