import heapq

def solution(operations):
    answer = []
    heap=[] #최소 힙
    max_heap=[] #최대 힙
    
    for operation in operations:
        op,num=operation.split()
        num=int(num)
        if op=='I': #큐에 숫자 삽입
            heapq.heappush(heap,num)
        else:
            if heap:
                if num==1: #큐에서 최댓값 삭제
                    max_value=max(heap)
                    heap.remove(max_value)
                else: #큐에서 최솟값 삭제
                    min_value=heapq.heappop(heap)
    
    if heap: #큐가 비어있지 않은 경우
        answer=[max(heap),heapq.heappop(heap)]
    else: #큐가 비었을 경우
        answer=[0,0]
    
    return answer