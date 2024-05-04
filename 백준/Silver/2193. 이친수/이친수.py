import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
dp[1]=1

#이전 수가 0일 경우 - 1,0 추가
#이전 수가 1일 경우 - 0 추가
#1로 끝나는 경우의 수 - dp[i-1]
#0으로 끝나는 경우의 수 - dp[i-2]
for i in range(2,n+1):
  dp[i]=dp[i-1]+dp[i-2]

print(dp[n])