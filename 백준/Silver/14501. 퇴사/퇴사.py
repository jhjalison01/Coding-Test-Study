import sys
input=sys.stdin.readline
#n 입력 받기
n=int(input())
#상담 일정 입력 받기
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))
#dp 테이블 초기화
dp=[0]*(n+1)
#dp 진행(보텀업)
for i in range(n):
  for j in range(i+data[i][0],n+1):
    #i번째 날짜에 상담했을 시 얻을 수 있는 최대 수익을 dp[j]에 저장
    if dp[j]<dp[i]+data[i][1]:
      dp[j]=dp[i]+data[i][1]

print(dp[-1])