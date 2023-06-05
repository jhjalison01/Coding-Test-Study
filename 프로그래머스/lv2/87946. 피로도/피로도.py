answer=0

#백트래킹 구현
def dfs(k,temp,dungeons,visited):
    global answer
    #temp 값이 answer 보다 커지면 answer 업데이트
    if temp>answer:
        answer=temp
    #
    for i in range(len(dungeons)):
        #던전을 가지 않았고 현재 피로도가 최소 필요 피로도보다 클 때
        if not visited[i] and k>=dungeons[i][0]:
            visited[i]=True
            #k에 소모 피로도를 빼고 temp를 1 더한 값을 인수로 전달
            dfs(k-dungeons[i][1],temp+1,dungeons,visited)
            visited[i]=False

def solution(k, dungeons):
    global answer
    visited = [False]*len(dungeons)
    dfs(k,0,dungeons,visited) #백트래킹 실행
    return answer