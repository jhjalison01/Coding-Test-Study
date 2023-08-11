#정수 x 입력받기
x=int(input())
#dp 테이블 초기화
dp=[0]*(x+1)

for i in range(2,x+1):
  #현재의 수에서 1을 빼는 경우
  dp[i]=dp[i-1]+1
  #3으로 나누어 떨어지는 경우
  if i%3==0:
    dp[i]=min(dp[i],dp[i//3]+1)
  #2로 나누어 떨어지는 경우
  if i%2==0:
    dp[i]=min(dp[i],dp[i//2]+1)
#연산하는 횟수의 최솟값을 출력
print(dp[x])