import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
nums=deque()

for i in range(1, n+1):
  nums.append(i)

while nums:
  print(nums.popleft(), end=" ")
  nums.rotate(-1)