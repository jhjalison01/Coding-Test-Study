#투 포인터 사용
def solution(gems):
    answer = [0,len(gems)]
    n=len(set(gems))
    left,right=0,0
    dict={gems[0] : 1}
    
    while left<len(gems) and right<len(gems):
        #보석을 다 선택한 경우
        if len(dict)==n:
            #최소 거리보다 작을 경우
            if right-left<answer[1]-answer[0]:
                answer=[left,right]
            else: #최소 거리보다 크거나 같을 경우
                dict[gems[left]]-=1
                if dict[gems[left]]==0: # 보석 개수가 0이 될 경우 삭제
                    del dict[gems[left]]
                left+=1 #left를 오른쪽으로 한 칸 옮긴다.
        else:
            right+=1 #right을 오른쪽으로 한 칸 옮긴다.
            if right==len(gems):
                break
            #key 값이 존재하면 value에 1 더하기, 존재하지 않을 경우 대입
            dict[gems[right]]=dict.get(gems[right],0)+1
                
    return [answer[0]+1,answer[1]+1]