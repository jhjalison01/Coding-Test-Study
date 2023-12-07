import sys
input=sys.stdin.readline
import heapq
INF=int(1e9)

n=int(input()) #도시 개수
m=int(input()) #버스 개수

#도시 지도 정보 입력받기
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

start,end=map(int,input().split())
answer=0
money=[INF]*(n+1)

def sol(start):
  q=[]
  #시작 노드 큐에 넣기
  heapq.heappush(q,(0,start))
  money[start]=0
  while q:
    mon, now=heapq.heappop(q)
    #이미 처리한 노드일 경우
    if money[now]<mon:
      continue
    #현재 노드와 연결된 노드 확인
    for i in graph[now]:
      cost=mon+i[1]
      if cost<money[i[0]]:
        money[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
  

sol(start)
print(money[end]) #도착 도시까지 드는 최소 비용 출력