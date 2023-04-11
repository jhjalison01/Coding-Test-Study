#이것이 취업을 위한 코딩 테스트다 Chapter6 정렬 실전문제4 두 배열의 원소 교체
import sys

n,k=map(int,sys.stdin.readline().split())     #N, K 입력 받기
a=list(map(int,sys.stdin.readline().split())) #배열 A 입력 받기
b=list(map(int,sys.stdin.readline().split())) #배열 B 입력 받기

a.sort() #배열 A를 오름차순으로 정렬
b.sort(reverse=True) # 배열 B를 내림차순으로 정렬

#첫 번째 인덱스부터 두 배열의 원소를 비교
for i in range(k):
  if a[i]<b[i]: # 배열 A의 원소가 배열 B의 원소보다 작은 경우
    a[i], b[i] = b[i], a[i] #두 원소를 교체
  else: #A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
    break

print(sum(a)) #배열 A의 모든 원소의 합 출력
