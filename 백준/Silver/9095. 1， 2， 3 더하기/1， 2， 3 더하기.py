#테스트 케이스 개수
t=int(input())
#dp 테이블 초기화
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
#4부터 10까지 각각 값을 구하기
#n>3 일 때 f(n)=f(n-1)+f(n-2)+f(n-3)
for i in range(4,11):
  dp[i]=sum(dp[i-3:i])

for i in range(t):
  n=int(input())
  print(dp[n])