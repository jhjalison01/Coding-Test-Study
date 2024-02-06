import sys
input=sys.stdin.readline
from itertools import combinations

n=int(input()) #n: 재료 개수
flavor=[] #flavor: 각 재료의 신맛, 쓴맛
for i in range(n):
  flavor.append(list(map(int,input().split())))

INF=int(1e9)
answer=INF

for i in range(1,n+1):
  for cases in combinations(flavor,i): #조합 구하기
    #신맛은 곱이고, 쓴맛은 합
    sour=1
    bitter=0
    for case in cases:
      sour*=case[0]
      bitter+=case[1]
    answer=min(answer,abs(sour-bitter))
    
#신맛과 쓴맛의 차이가 가장 작은 요리의 차이 출력
print(answer)