import sys
import heapq
input=sys.stdin.readline
#연산 개수 입력 받기
n=int(input())

heap=[]
for i in range(n):
  x=int(input())
  if x==0:
    if len(heap)==0: #힙이 비었을 경우
      print(0) #0 출력
    else:
      print(heapq.heappop(heap)[1]) #x 출력, 제거
  else:
    #x의 절댓값과 x를 힙에 넣기
    heapq.heappush(heap,(abs(x),x))