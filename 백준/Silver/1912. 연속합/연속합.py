import sys
input=sys.stdin.readline

#n: 계단의 개수
n=int(input())
data=list(map(int,input().split()))

#이전까지 모든 숫자의 합 중 최댓값을 기록한다.
for i in range(1,n):
  data[i]=max(data[i],data[i]+data[i-1])

print(max(data))