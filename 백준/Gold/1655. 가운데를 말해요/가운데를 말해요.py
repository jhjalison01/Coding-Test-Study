import sys
input=sys.stdin.readline
import heapq

n=int(input()) #n: 정수의 개수
left=[] #중간값보다 작은 값 저장
right=[] #중간값보다 큰 값 저장

for i in range(n):
  num=int(input())
  if len(left)==len(right):
    #left를 최대 힙으로 만들어 첫 원소가 중간값이 되게 한다.
    heapq.heappush(left,(-num,num))
  else:
    #right는 최소 힙
    heapq.heappush(right,(num,num))
  #right의 최소값이 left의 최대값(중간값) 보다 작을 경우
  if right and right[0][1]<left[0][1]:
    l=heapq.heappop(left)[1]
    r=heapq.heappop(right)[1]
    heapq.heappush(left,(-r,r))
    heapq.heappush(right,(l,l))
  print(left[0][1]) #중간값 출력