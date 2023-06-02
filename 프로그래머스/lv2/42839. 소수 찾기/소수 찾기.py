#순열 모듈
from itertools import permutations

#소수인지 판별하는 함수
def is_prime_number(num):
    if num<2:
        return False
    for x in range(2,num):
        if num%x==0:
            return False
    return True

def solution(numbers):
    answer = 0
    num=[]
    
    for i in range(1,len(numbers)+1):
        #순열 모듈 사용해서 나올 수 있는 모든 수 조합
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    #중복 제거, 수를 정수로 바꾸기
    per=list(set(map(int,sum(num,[]))))
    
    #소수인지 확인
    for x in per:
        if is_prime_number(x):
            answer+=1
    return answer