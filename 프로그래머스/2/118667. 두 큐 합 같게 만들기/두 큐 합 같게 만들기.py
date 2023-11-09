from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    total1=sum(queue1)
    total2=sum(queue2)
    #queue1의 원소가 queue2로 전부 이동하고, queue2의 원소만 queue1으로 이동하고, 남은 queue2의 원소가 queue1으로 이동하는 경우는 queue1의 길이의 3배이다. 따라서 이 이상 반복하는 것은 의미가 없다.
    limit = (len(queue1))*3
    if (total1+total2)%2==1:
        return -1

    while True:
        if answer==limit:
            return -1
        
        #total1이 total2보다 작을 경우
        if total1<total2:
            temp=queue2.popleft()
            queue1.append(temp)
            total1+=temp
            total2-=temp
            answer+=1
        #total1이 total2보다 클 경우
        elif total1>total2:
            temp=queue1.popleft()
            queue2.append(temp)
            total1-=temp
            total2+=temp
            answer+=1
        #total과 target 값이 같을 경우 반복 중지
        else:
            return answer