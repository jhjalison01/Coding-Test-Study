#백준 2407번 조합
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a,b=1,1

for i in range(m):
  a*=(n-i)

for i in range(m):
  b*=(m-i)

print(a//b)