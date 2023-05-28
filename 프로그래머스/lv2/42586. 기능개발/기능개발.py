from collections import deque
def solution(progresses, speeds):
    answer = []
    #작업 직도, 작업 속도를 큐로 바꾸기
    progresses=deque(progresses)
    speeds=deque(speeds)
    
    while progresses: #작업이 모두 배포될 때까지 수행
        progresses=deque([x+y for x,y in zip(progresses, speeds)]) #작업 진도와 작업 속도 더하기
        count=0 #배포 하는 작업의 개수
        while progresses: 
            if progresses[0]>=100: #맨처음 작업이 100보다 클 경우
                progresses.popleft() #해당 작업을 배포
                speeds.popleft() #해당 작업 속도 삭제
                count+=1 #배포될 작업 수 1 더하기
            else:
                break #맨처음 작업을 끝나지 않았다면 배포 시도 종료
        if count>0: #배포될 작업이 있을 경우
            answer.append(count) #작업 배포
    return answer