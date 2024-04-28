import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dis=[0]
for _ in range(n):
  dis.append(int(input()))

#dp[i][j] - 달린 거리
#: i - i분, j - 지침 지수
dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
  #직전에도 쉬고 현재 분에도 쉰 거리
  dp[i][0] = dp[i-1][0]
  for j in range(1,m+1):
    #i분까지 달린 거리
    dp[i][j] = dp[i-1][j-1]+dis[i]
    dp[i][0] = max(dp[i][0],dp[i-j][j])

#최대 거리 출력
print(dp[-1][0])