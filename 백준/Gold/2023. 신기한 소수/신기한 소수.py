import sys
input=sys.stdin.readline

#에라토스테네스의 체로 소수인지 확인
def is_prime(n):
  if n < 2:
      return False
  for i in range(2, int(n**0.5)+1):
      if n % i == 0:
          return False
  return True

n=int(input())

def sol(num):
  if len(str(num)) == n:
    print(num)
    return
  for i in range(10):
    k = num*10+i
    #num에 i 붙인 것이 소수일 경우
    if is_prime(k):
      sol(k)

#일의 자리 숫자 중 소수로 시
sol(2)
sol(3)
sol(5)
sol(7)