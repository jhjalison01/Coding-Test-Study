from collections import deque

def solution(prices):
    answer = []
    #큐로 바꾸기
    queue=deque(prices)
    #큐가 빌 때까지 실행
    while queue:
        price=queue.popleft()
        cnt=0
        for q in queue:
            cnt+=1
            #가격이 떨어질 경우 반복 종료
            if price>q:
                break
        answer.append(cnt) #가격이 떨어지지 않은 기간 추가
        
    return answer