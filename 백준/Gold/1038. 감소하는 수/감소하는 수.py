import sys
input=sys.stdin.readline
from itertools import combinations

n=int(input())

nums=[] #감소하는 수 저장할 리스트

for i in range(1,11): #0~9까지 숫자를 사용하므로 1~10까지 조합을 만듦
  for comb in combinations(range(0,10),i): #0~9로 조합 만들기
    comb=list(comb)
    comb.sort(reverse=True) #감소하는 수로 만들기
    nums.append(int("".join(map(str,comb)))) #정수로 바꾸어 저장
    
#오름차순으로 정렬
nums.sort()

#N번째 감소하는 수가 없을 경우
if n>=len(nums):
  print(-1)
else:
  print(nums[n])