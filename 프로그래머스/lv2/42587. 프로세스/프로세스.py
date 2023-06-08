from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque(priorities) #우선순위 리스트를 deque로 바꾸기
    while q:
        x=max(q)
        temp=q.popleft()
        if temp<x: #대기 큐에 우선순위가 더 높은 프로세스가 있을 때
            q.append(temp) #큐에 다시 넣기
            #알고싶은 프로세스 위치 변경
            if location==0:
                  location=len(q)-1
            else:
                  location-=1
        else: #큐에 우선순위가 더 높을 때
            answer+=1 #프로세스 실행
            if location==0: #해당 프로세스가 몇 번째 실행되는지 알고싶은 프로세스일 때
                break #반복 중지
            else:
                location-=1 #아니라면 프로세스 위치 변경
    return answer


