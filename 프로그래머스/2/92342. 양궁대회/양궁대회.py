def solution(n, info):
    answer = []
    diff=0 #점수 차
    ryan=[0]*11
    
    #cnt: 쏜 화살 수, idx: 현재 탐색하는 과녁 번호
    def dfs(cnt,idx):
        nonlocal answer, diff, ryan
        if cnt==n:
            total=0 #라이언 점수
            p_total=0 #어피치 점수
            
            #각각 총 점수 구하기
            for i in range(11):
                if ryan[i]>info[i]:
                    total+=10-i
                elif info[i]!=0 and ryan[i]<=info[i]:
                    p_total+=10-i
                    
            #라이언이 이긴 경우
            if total>p_total:
                #점수 차가 더 많이 났다면 갱신
                if diff<total-p_total:
                    diff=total-p_total
                    answer=ryan.copy()
                #동점일 경우 낮은 점수를 더 많이 쐈다면 갱신
                elif diff == total-p_total:
                    for i in range(10,-1,-1):
                        if ryan[i]<answer[i]:
                            break
                        elif ryan[i]>answer[i]:
                            answer=ryan.copy()
                            break
            return
        
        for i in range(idx,11):
            ryan[i]+=1 #i점을 맞춤
            dfs(cnt+1,i) #dfs 실행
            ryan[i]-=1 #원상태로 복구
        
        
    dfs(0,0)
    
    if not answer:
        answer=[-1]
    
    return answer