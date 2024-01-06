import math

def check(num_bin,prev_parent):
    mid=len(num_bin)//2
    if num_bin:
        son=(num_bin[mid]=='1')
    else:
        return True
    
    #자식이 존재하면 부모도 존재해야함
    if son and not prev_parent: #자식은 존재하지만 부모가 존재하지 않을 경우
        return False
    else: #num_bin[mid] 노드를 기준으로 왼쪽 트리, 오른쪽 트리 검사
        return check(num_bin[:mid],son) and check(num_bin[mid+1:],son)
        
def sol(number):
    if number==1:
        return 1
    #이진수로 변환
    num_bin=bin(number)[2:]
    #2^n-1꼴의 자릿수 구하기
    digit=2**(int(math.log(len(num_bin),2))+1)-1
    #남은 자릿수만큼 0 추가
    num_bin="0"*(digit-len(num_bin))+num_bin
    #자식 노드가 있을 경우 부모 노드가 모두 존재해야함
    if num_bin[len(num_bin)//2]=='1' and check(num_bin,True): return 1
    else: return 0

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(sol(number))
    return answer