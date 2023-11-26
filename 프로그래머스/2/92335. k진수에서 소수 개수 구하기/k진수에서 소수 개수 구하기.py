import math

#10진수를 k진수로 변환
def sol(n,k):
    temp=""
    
    while n>0:
        n,mod=divmod(n,k)
        temp+=str(mod)
    return temp[::-1]

#소수인지 판별
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n%i==0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    num=sol(n,k) #k진수로 바꾸기
    data=list(num.split("0")) #0으로 숫자 나누기
    for x in data:
        if x:
            x=int(x)
            if is_prime(x): #소수인지 확인
                answer+=1
    
    return answer