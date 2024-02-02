import sys
input=sys.stdin.readline

n=int(input())

wine=[0]
for i in range(n):
  wine.append(int(input()))
  
dp=[0]*(n+1)
dp[1]=wine[1]
if n > 1:
  dp[2]=wine[1]+wine[2]

#1. i번째 와인을 안 먹는 경우 2. 연속으로 와인을 안 먹은 경우 3. 연속 2번 와인을 먹은 경우
for i in range(3,n+1):
  dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

#최대로 마실 수 있는 포도주의 양 출력
print(dp[n])