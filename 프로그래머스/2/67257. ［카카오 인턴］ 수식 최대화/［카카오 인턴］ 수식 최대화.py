from itertools import permutations
import re

def calculate(a,b,op):
    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b

def solution(expression):
    answer = 0
    operator=["+","-","*"]
    ops=set()
    num=""
    result=[]
    #expression 안에 들어 있는 연산자 저장
    for x in expression:
        if x in operator:
            ops.add(x)
    #연산자 우선순위
    op_lists=list(permutations(ops,len(ops)))
    #숫자와 문자열을 분리해서 저장
    expression = re.split("([^0-9])",expression)
    for op_list in op_lists:
        exp=expression
        for op in op_list: #우선순위 순서대로 계산
            stack=[]
            for e in exp:
                #스택 마지막 요소가 해당 연산자일 경우
                if stack and stack[-1]==op:
                    stack.pop()
                    stack[-1]=calculate(int(stack[-1]),int(e),op) #계산하여 스택에 넣기
                else:
                    stack.append(e)
            exp=stack
        result.append(abs(exp[0]))
                
    return max(result)