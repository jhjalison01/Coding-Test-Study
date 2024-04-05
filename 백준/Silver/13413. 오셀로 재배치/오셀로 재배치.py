#W랑 B가 있으면 더 큰 수를 출력
#ex) data1에 입력받은 것이 만약 WBB라면 W랑 B는 서로 위치 바꾸어서 한 번, B하나 남은건 W로 바꾸어 줄테니까 총 2번.

import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
  n=int(input())
  data1=input()
  data2=input()
  cnt_b=0
  cnt_w=0
  for i in range(n):
    if data1[i]!=data2[i]:
      if data1[i]=='B':
        cnt_b+=1
      else:
        cnt_w+=1
  print(max(cnt_b,cnt_w))