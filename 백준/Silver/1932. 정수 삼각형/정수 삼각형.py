import sys
input=sys.stdin.readline

#n: 삼각형의 크기
n=int(input())
dp=[]
for i in range(n):
  dp.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(len(dp[i])):
    if j==0: # 맨 왼쪽일 경우
      dp[i][j]+=dp[i-1][j]
    elif j==len(dp[i])-1: # 맨 오른쪽일 경우
      dp[i][j]+=dp[i-1][j-1]
    else:
      dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])

#최대 합 출력하기
print(max(dp[n-1]))