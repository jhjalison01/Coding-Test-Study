import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
data=deque(enumerate(map(int,input().split())))

for i in range(n):
  idx,num=data.popleft()
  #터진 풍선 번호 출력
  print(idx+1,end=" ")
  #deque.rotate(num)을 하면 deque를 num만큼 회전한다.(양수면 오른쪽, 음수면 왼쪽)
  if num>0:
    data.rotate(-(num-1))
  elif num<0:
    data.rotate(-num)