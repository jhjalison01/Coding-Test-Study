from collections import deque
        
def solution(numbers, target):
    answer=0
    q=deque()
    n=len(numbers)
    q.append([numbers[0],0])
    q.append([-numbers[0],0])
    while q:
        temp,index=q.popleft()
        index+=1
        if index<n:
            q.append([temp+numbers[index],index])
            q.append([temp-numbers[index],index])
        else:
            if temp==target:
                answer+=1

    return answer