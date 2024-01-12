import sys
input=sys.stdin.readline

#숫자 입력 받기
nums=list(input().rstrip())
answer=-1

#30배수 - 3의 배수와 10의 배수의 특징을 갖음
#3의 배수 - 각 자리의 숫자의 합이 3의 배수
#10의 배수 - 끝자리가 0
total=0
for i in nums:
  total+=int(i)
if '0' in nums and total%3==0:
  nums.sort(reverse=True)
  answer=int("".join(nums))

print(answer)