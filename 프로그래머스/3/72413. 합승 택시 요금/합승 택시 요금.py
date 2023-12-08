import heapq

def solution(n, s, a, b, fares):
    INF=int(1e9)
    answer = INF
    
    graph=[[] for _ in range(n+1)]
    for f in fares:
        node1,node2,fee=f
        graph[node1].append((node2,fee))
        graph[node2].append((node1,fee))
        
    def sol(start):
        q=[]
        #최소 비용 테이블을 무한대로 초기화
        money=[INF]*(n+1)
        #큐에 처음 노드 삽입
        heapq.heappush(q,(0,start))
        #시작 노드로 가는 비용 0
        money[start]=0
        while q:
            mon,now=heapq.heappop(q)
            #현재 노드가 이미 처리된 경우
            if money[now]<mon:
                continue
            for g in graph[now]:
                cost=mon+g[1]
                if cost<money[g[0]]:
                    money[g[0]]=cost
                    heapq.heappush(q,(cost,g[0]))
        return money
    
    #mon_list[i][j] - i부터 j까지 가는데 드는 최소 비용
    mon_list=[[]]
    for i in range(1,n+1):
        mon_list.append(sol(i))
        
    #시작 지점부터 a,b까지의 최소 비용 구하기
    for i in range(1,n+1):
        answer=min(answer,mon_list[s][i]+mon_list[i][a]+mon_list[i][b])
        
    return answer