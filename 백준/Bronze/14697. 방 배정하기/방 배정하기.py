import sys
input=sys.stdin.readline

a,b,c,n=map(int,input().split())
result=0

for i in range(n//a+1):
  for j in range(n//b+1):
    for k in range(n//c+1):
      #합이 n이 될 경우
      if i*a+j*b+k*c==n:
        result=1

print(result)