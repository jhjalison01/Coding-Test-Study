import sys
input=sys.stdin.readline

n=int(input())

#dp[자리 수][앞에 오는 숫자]=경우의 수
dp=[[0]*10 for _ in range(n+1)]

#자릿수가 1인 경우 경우의 수가 모두 1
for i in range(1,10):
  dp[1][i]=1

for i in range(2,n+1):
  for j in range(10):
    if j==0: #앞에 오는 숫자가 0일 경우 
      dp[i][j]=dp[i-1][1]
    elif j==9: #앞에 오는 숫자가 9일 경우
      dp[i][j]=dp[i-1][8]
    else:
      dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n])%1000000000)