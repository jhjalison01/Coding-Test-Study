import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
data=list(map(int,input().split()))

data.sort()
left,right=0,n-1
answer=0

#투 포인터 사용
while left<right:
  sum_num=data[left]+data[right]
  #합이 m일 경우
  if sum_num==m:
    answer+=1
    left+=1
    right-=1
  #합이 m보다 클 경우 right를 왼쪽으로 이동
  elif sum_num>m:
    right-=1
  #합이 m보다 작을 경우 left를 오른쪽으로 이동
  else:
    left+=1

print(answer)