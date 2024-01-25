import sys
input=sys.stdin.readline

#n: 계단의 개수
n=int(input())

score=[0]*301
for i in range(1,n+1):
  score[i]=int(input())

dp=[0]*301
dp[1]=score[1]
dp[2]=score[1]+score[2]
dp[3]=max(score[2],score[1])+score[3]

for i in range(4,n+1):
  #전전칸에서 올라온 경우 or 직전 칸에서 올라온 경우
  dp[i]=max(dp[i-2],dp[i-3]+score[i-1])+score[i]

print(dp[n])