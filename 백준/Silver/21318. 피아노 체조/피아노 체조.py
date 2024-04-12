import sys
input=sys.stdin.readline

#악보의 개수
n=int(input())
#악보 난이도
diff = list(map(int,input().split()))

dp=[0]*n
for i in range(1,n):
  if diff[i-1]>diff[i]:
    dp[i]=dp[i-1]+1
  else:
    dp[i]=dp[i-1]

#질문 개수
q=int(input())

for _ in range(q):
  x,y=map(int,input().split())
  #x부터 y까지 틀린 악보 개수 출력
  print(dp[y-1]-dp[x-1])