import sys
input=sys.stdin.readline
import math

T=int(input())

for _ in range(T):
  n,m=map(int,input().split())
  # mCn = m! / (m-n)!n!
  bridge = math.factorial(m) // (math.factorial(m-n) * math.factorial(n))
  print(bridge)