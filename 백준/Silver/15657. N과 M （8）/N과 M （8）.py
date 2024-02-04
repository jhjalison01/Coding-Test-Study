import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement

n,m=map(int,input().split())

nums=list(map(int,input().split()))
nums.sort() #수열은 오름차순이 되어야 함

#중복 조합 라이브러리 사용
for num in combinations_with_replacement(nums,m):
  for i in num:
    print(i,end=" ")
  print()