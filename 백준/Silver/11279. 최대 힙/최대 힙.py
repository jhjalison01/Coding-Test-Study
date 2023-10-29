import sys
import heapq
input=sys.stdin.readline
  
N=int(input())

heap=[]
for i in range(N):
  x=int(input())
  if x==0:
    if heap: #힙에 정수가 있을 경우
      print(abs(heapq.heappop(heap))) #가장 큰 수 출력
    else: #힙이 비어있을 경우
      print(0) #0 출력
  else: #x가 0이 아닐 경우
    heapq.heappush(heap,-x) #힙에 저장, x를 음수로 저