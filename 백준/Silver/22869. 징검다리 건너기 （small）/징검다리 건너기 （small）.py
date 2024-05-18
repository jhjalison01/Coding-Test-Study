import sys
input=sys.stdin.readline

N,K=map(int,input().split())
rocks=list(map(int,input().split()))
dp=[0]*N
#첫번째 돌은 갈 수 있음
dp[0]=1

#i번째 돌에서 j번째 돌로 이동 가능한지 확인
for i in range(N-1):
  for j in range(i+1,N):
    if dp[i] and (j-i)*(1+abs(rocks[i]-rocks[j]))<=K:
      dp[j]=1

if dp[-1]:
  print("YES")
else:
  print("NO")