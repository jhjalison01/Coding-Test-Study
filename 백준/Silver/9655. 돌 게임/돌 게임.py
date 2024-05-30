import sys
input=sys.stdin.readline

n=int(input())
dp=[-1]*1001

dp[1] = 1 #n=1 일 경우 상근이가 마지막 돌 가져가서 상근이가 이김
dp[2] = 0 #n=2 일 경우 상근이가 한 개 가져간 후 창영이가 마지막 돌 가져가서 창영이가 이김
dp[3] = 1 #n=3 일 경우 상근이가 마지막 돌을 포함해서 3개 가져가므로 상근이가 이김

for i in range(4,n+1):
  if dp[i-1] ==1 or dp[i-3]==1:
    dp[i] = 0
  else:
    dp[i]=1

if dp[n]:
  print("SK") #상근이가 이김
else:
  print("CY") #창영이가 이김