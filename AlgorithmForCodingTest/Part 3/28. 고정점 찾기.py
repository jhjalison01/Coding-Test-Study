#이것이 취업을 위한 코딩 테스트다 Part3 이진 탐색 28. 고정점 찾기

#이진 탐색 구현
def binary_search(data,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  #고정점을 찾은 경우 인덱스 반환
  if data[mid]==mid:
    return mid
  #중간점이 가리키는 위치의 값보다 중간점이 큰 경우 - 오른쪽 확인
  elif data[mid]<mid:
    return binary_search(data,mid+1,end)
  #중간점이 가리키는 위치의 값보다 중간점이 작은 경우 - 왼쪽 확인
  elif data[mid]>mid:
    return binary_search(data,start,mid-1)


n=int(input())
data=list(map(int,input().split()))

answer=binary_search(data,0,n-1)

#고정점이 없느 경우 -1 출력
if answer==None:
  print(-1)
else: #고정점이 있는 경우 인덱스 출
  print(answer)
