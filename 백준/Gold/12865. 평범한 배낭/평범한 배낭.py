import sys
input=sys.stdin.readline

n,k=map(int,input().split())
data=[[0,0]]
for _ in range(n):
  data.append(list(map(int,input().split())))

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,k+1):
    weight = data[i][0]
    value = data[i][1]
    if j<weight:
      dp[i][j]=dp[i-1][j]
    else:
      dp[i][j]=max(dp[i-1][j], value+dp[i-1][j-weight])
  
#물건들의 가치합의 최댓값 출력
print(dp[n][k])