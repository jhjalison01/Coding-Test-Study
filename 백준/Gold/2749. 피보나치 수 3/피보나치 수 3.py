import sys
input=sys.stdin.readline

#피사노 주기 - 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게 된다.
#나누려는 수가 10^k이고 이때의 k가 2보다 크다면 주기는 항상 15*10^(k-1)이다.

K=1500000 #주기 길이
P=1000000

n=int(input())
n=n%K #주기 길이만큼 나누어 주기

dp=[0]*(n+1)
dp[1]=1

for i in range(2,n+1):
  dp[i]=(dp[i-1]+dp[i-2])%P #피보나치 수 구하기

print(dp[n])