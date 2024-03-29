#이것이 취업을 위한 코딩 테스트다 Part3 구현 14. 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    length=len(weak)
    #길이를 늘려 '원형'을 일자 형태로 표현
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1
    #0부터 length-1까지의 위치를 시작점으로 설정
    for start in range(length):
        #친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count=1 #투입할 친구의 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position=weak[start]+friends[count-1]
            #시작점부터 모든 취약 지점 확인
            for index in range(start,start+length):
                #점검할 수 있는 위치를 벗어난 경우
                if position<weak[index]:
                    count+=1 #새로운 친구를 투입
                    if count>len(dist): #더 투입이 불가능한 경우
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count) #최솟값 계산
    if answer>len(dist):
        return -1
    return answer
