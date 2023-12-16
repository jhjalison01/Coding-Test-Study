import heapq
def solution(scoville, K):
    answer = 0
    #schoville를 heap으로 만든다.
    heapq.heapify(scoville)
    #가장 작은 수가 K 이상이 될 때까지 반복
    while scoville[0]<K:
        #모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
        if len(scoville)==1:
            answer=-1
            break
        a=heapq.heappop(scoville) #가장 작은 수
        b=heapq.heappop(scoville) #두 번째로 작은 수
        heapq.heappush(scoville,a+b*2) #새로운 음식 만들기
        answer+=1 #횟수 증가
    
    return answer