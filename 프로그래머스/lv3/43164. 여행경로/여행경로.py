def solution(tickets):
    answer = []
    #각 티켓을 확인한 정보를 리스트로 표현
    visited=[False]*len(tickets)
    
    #dfs 구현
    def dfs(airport,path):
        #경로를 찾았을 경우 answer에 넣기
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        for idx, ticket in enumerate(tickets):
            #현재 공항과 티켓의 공항이 같고 가지 않은 공항일 경우 dfs 실행
            if airport==ticket[0] and visited[idx]==False:
                visited[idx]=True
                dfs(ticket[1],path+[ticket[1]]) #다음 공항과 추가된 경로를 매개변수로 대입
                visited[idx]=False
    #dfs 실행, 처음 공항은 ICN
    dfs("ICN",["ICN"])
    #찾은 경로를 오름차순으로 정렬하여 알파벳 순서가 앞서는 경로를 리턴
    answer.sort()
    return answer[0]