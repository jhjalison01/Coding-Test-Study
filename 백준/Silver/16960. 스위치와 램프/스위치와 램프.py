import sys
input=sys.stdin.readline
from collections import defaultdict

#스위치의 수, 램프의 수
n,m=map(int,input().split())
lamps=defaultdict(int)

#스위치 정보 입력 받기
switches=[]
for _ in range(n):
  switch = list(map(int,input().split()))
  switches.append(switch)
  #각 램프마다 연결된 스위치 수 저장
  for i in range(1,switch[0]+1):
    lamps[switch[i]]+=1

result=0
#스위치 하나를 껐을 때 그 스위치에 연결된 모든 랜턴이 2개 이상의 스위치와 연결되어 있을 경우 result=1이 됨
for switch in switches:
  flag=True
  for i in range(1, len(switch)):
    if lamps[switch[i]]>=2:
      continue
    else:
      flag=False
      break
      
  if flag:
    result=1
    break
    
print(result)