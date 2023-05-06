#이것이 취업을 위한 코딩 테스트다 Part3 그리디 6. 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    length=len(food_times)
    
    q=[]
    #음식별 필요 시간을 우선순위 큐에 넣는다.
    for i in range(length):
        heapq.heappush(q,(food_times[i],i+1))
        
    sum_value=0 #먹기 위해 사용한 시간
    previous=0 #직전에 다 먹은 음식 시간
    
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0] #현재 음식 시간
        sum_value+=(now-previous)*length
        length-=1 #다 먹은 음식 제외
        previous=now #이전 음식 먹은 시간 재설정
    
    result=sorted(q, key=lambda x:x[1]) #남은 음식들을 번호 기준으로 정렬
    answer=result[(k-sum_value)%length][1] #몇 번째 음식인지 확인
    
    return answer
