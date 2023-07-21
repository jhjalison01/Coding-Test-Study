from collections import deque

def solution(begin, target, words):
    if target not in words:  # words 리스트에 target값이 없을 경우 0 리턴
        return 0
    
    #큐에 begin과 cnt 값 넣기
    queue=deque()
    queue.append((begin,0))
    
    #bfs 구현
    while queue:
        x, cnt=queue.popleft() #큐에서 단어 꺼내기
        
        if x==target: #x가 target이면 cnt 리턴
            return cnt
        #해당 단어를 words에 있는 단어들과 비교하여 바꿀 수 있는 단어 확인
        for i in range(len(words)):
            diff=0
            for j in range(len(x)):
                #알파벳이 다르다면 diff에 1 더하기
                if x[j]!=words[i][j]:
                    diff+=1
            #알파벳이 한 가지만 다를 경우
            if diff==1:
                #큐에 추가
                queue.append((words[i],cnt+1))
    return 0 #변환할 수 없는 경우 0을 리턴