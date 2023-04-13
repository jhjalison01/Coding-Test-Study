#이것이 취업을 위한 코딩 테스트다 Chapter7 이진탐색 실전문제2 부품 찾기
import sys

#N(가게의 부품 개수) 입력 받기
n=int(sys.stdin.readline().rstrip())
n_list=list(map(int, sys.stdin.readline().split())) #가게에 있는 부품 번호 입력 받기

n_list.sort() #이진 탐색을 위해 부품 번호를 정렬
#M(손님이 요청한 부품 개수) 입력 받기
m=int(sys.stdin.readline().rstrip())
m_list=list(map(int, sys.stdin.readline().split())) #손님이 요청한 부품 번호 입력 받기

#이진 탐색 구현
def binary_search(array, target, start, end):
  #start가 end보다 크면 해당 부품 번호가 없으므로 none을 반환
  if start>end:
    return None
  else:
    mid=(start+end)//2 #중간점의 값 부여
    if array[mid]==target: #찾은 경우 중간점 인덱스 반환
      return mid
    elif target<mid: # 중간점 값보다 작을 때 왼쪽 확인
      return binary_search(array, target, start,mid-1)
    else: #중간점 값보다 클 때 오른쪽 확인
      return binary_search(array, target, mid+1, end)

#손님이 요청한 부품 번호를 하나씩 확인
for i in m_list:
  if binary_search(n_list,i,0,n-1)==None:
    print("no", end=" ")
  else:
    print("yes", end=" ")
