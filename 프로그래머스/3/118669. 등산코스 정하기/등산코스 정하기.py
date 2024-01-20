import heapq
INF=int(1e9)

def solution(n, paths, gates, summits):
    #graph: 등산로 정보
    graph=[[] for _ in range(n+1)]
    for a,b,w in paths:
        graph[a].append([b,w])
        graph[b].append([a,w])
        
    summits.sort()
    summits_set = set(summits)
    #다익스트라 알고리즘 구현
    def dijkstra():
        q=[]
        intensity=[INF]*(n+1)
        #모든 출입구를 우선순위 큐에 삽입
        for gate in gates:
            heapq.heappush(q,(0,gate))
            intensity[gate]=0
            
        while q:
            intens,now=heapq.heappop(q)
            #산봉우리이거나 더 큰 intensity일 경우 이동하지 않음
            if now in summits_set or intensity[now]<intens:
                continue
            #다음 노드로 이동
            for next_node, weight in graph[now]:
                new_intensity=max(weight, intens)
                if new_intensity<intensity[next_node]:
                    intensity[next_node]=new_intensity
                    heapq.heappush(q,(new_intensity,next_node))
        # 구한 intensity 중 가장 작은 값 반환
        # 거리가 같으면 산봉우리의 번호가 작은 것을 출력
        min_intensity = [-1, INF]
        for summit in summits:
            if intensity[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = intensity[summit]

        return min_intensity
    
    return dijkstra()