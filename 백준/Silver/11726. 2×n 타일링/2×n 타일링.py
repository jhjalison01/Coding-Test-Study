import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*1001
dp[1]=1
dp[2]=2
#i번째 경우의 수는 (i-1)과 (i-2)번째 경우의 수를 합한 것과 같음
for i in range(3,n+1):
  dp[i]=(dp[i-1]+dp[i-2])%10007

print(dp[n])