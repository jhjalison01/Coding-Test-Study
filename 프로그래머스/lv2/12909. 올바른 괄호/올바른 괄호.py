def solution(s):
    answer = True
    stack=[]
    
    for x in s:
        if x=='(': # '('은 스택에 넣기
            stack.append(x)
        else: # ')'일 경우
            if len(stack)==0: #stack이 비어 있는 경우 false 리턴
                return False
            elif stack and stack[-1]=='(': #stack에 요소가 있고 마지막 요소가 '('이면 마지막 요소를 제거
                stack.pop()
            
    
    if stack: #스택에 요소가 남아 있으면 올바르지 않은 괄호이다
        answer=False

    return answer