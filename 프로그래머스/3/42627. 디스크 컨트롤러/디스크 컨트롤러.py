import heapq

def solution(jobs):
    answer = 0
    time, j=0,0 #현재 시간, 처리한 작업 수
    previous=-1 #이전에 완료한 작업의 시작 시간
    heap=[]
    
    while j<len(jobs):
        for job in jobs:
            #작업 요청
            if previous<job[0]<=time:
                heapq.heappush(heap,[job[1],job[0]])
        if len(heap)>0:
            current=heapq.heappop(heap)
            previous=time
            time+=current[0] #작업 시간만큼 증가
            answer+=time-current[1] #요청부터 종료까지 걸린 시간
            j+=1
        else: #작업이 없을 경우 time 증가
            time+=1
    
    
    return int(answer/len(jobs))