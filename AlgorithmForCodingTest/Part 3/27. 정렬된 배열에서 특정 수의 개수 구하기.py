#이것이 취업을 위한 코딩 테스트다 Part3 이진 탐색 27. 정렬된 배열에서 특정 수의 개수 구하기

#bisect_left(list, data) : 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수
#bisect_right(list, data): 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수

from bisect import bisect_left, bisect_right

#구하고자 하는 데이터의 개수를 반환하는 함수
def count_by_range(data,left_value,right_value):
  right_index=bisect_right(data,right_value)
  left_index=bisect_left(data,left_value)
  print(right_index)
  print(left_index)
  return right_index-left_index

n,x=map(int,input().split())
data=list(map(int,input().split()))

#x인 원소 개수 구하기
answer=count_by_range(data,x,x)

#값이 x인 원소가 없을 경우
if answer==0:
  print(-1)
else: #원소의 개수 구하기
  print(answer)
