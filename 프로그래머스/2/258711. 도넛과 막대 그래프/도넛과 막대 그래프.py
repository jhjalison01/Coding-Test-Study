from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    
    edge_cnt=defaultdict(lambda: [0,0])
    for a,b in edges:
        edge_cnt[a][0]+=1 #나가는 간선
        edge_cnt[b][1]+=1 #들어오는 간선
        
    for node, item in edge_cnt.items():
        give=item[0]
        take=item[1]
        
        #생성한 정점 번호 찾기, 나가는 간선 2개 이상, 들어오는 간선 0개
        if give>=2 and take == 0:
            answer[0]=node
        #막대 모양 그래프의 수 확인, 마지막 도착 노드는 들어오는 간선만 있고 나가는 간선 없음
        elif give==0 and take>=1:
            answer[2]+=1
        #8자형 그래프의 수 확인, 들어오는 간선과 나가는 간선 모두 2개 이상
        elif give >=2 and take>=2:
            answer[3]+=1
    #나머지는 도넛 모양 그래프의 수
    answer[1]= edge_cnt[answer[0]][0] - answer[2] - answer[3]
        
    return answer