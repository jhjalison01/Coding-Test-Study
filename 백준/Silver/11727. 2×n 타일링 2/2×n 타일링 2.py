import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*1001

#초기값 지정
dp[1]=1
dp[2]=3

#dp[i-1]에서 2x1 타일 하나 붙이는 경우
#dp[i-2]에서 1x2 타일 2개 붙이는 경우 or 2x2 타일 붙이는 경우
for i in range(3, n+1):
  dp[i]=dp[i-1]+dp[i-2]*2

print(dp[n]%10007)