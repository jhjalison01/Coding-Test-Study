import sys
input=sys.stdin.readline

n=int(input())
answer=n

for num in range(1,n+1):
  cnt=0
  num=str(num)
  for i in range(len(num)-1):
    #연속된 두 개의 수의 차이
    cnt=int(num[0])-int(num[1])
    #각 자리가 등차수열을 이루지 않는 경우
    if cnt!=int(num[i])-int(num[i+1]):
      answer-=1
      break

print(answer)