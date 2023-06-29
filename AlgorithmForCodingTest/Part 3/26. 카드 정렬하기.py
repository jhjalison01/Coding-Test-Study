#이것이 취업을 위한 코딩 테스트다 Part3 정렬 26. 카드 정렬하기
#백준 1715번

import heapq

n=int(input())

#힙 자료구조 사용
heap=[]
answer=0

#힙에 숫자 카드 묶음의 크기 넣기
for i in range(n):
  data=int(input())
  heapq.heappush(heap,data)

for i in range(n-1):
  #힙 자료구조에 의해 작은 값부터 추출된다.
  one=heapq.heappop(heap)
  two=heapq.heappop(heap)
  answer+=one+two
  #카드 묶음을 합쳐서 힙에 다시 삽입
  heapq.heappush(heap,one+two)
  
print(answer)
