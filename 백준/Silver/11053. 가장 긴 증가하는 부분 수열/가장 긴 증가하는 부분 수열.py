import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
dp=[1]*n #dp[i]는 data[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(n):
  for j in range(i):
    if data[i]>data[j]: #현재 정수가 이전 정수보다 클 경우
      dp[i]=max(dp[i],dp[j]+1)

print(max(dp))