#이것이 취업을 위한 코딩 테스트다 Chapter6 정렬 실전문제2
import sys

n=int(sys.stdin.readline())

data=[]

# 입력값들을 리스트에 저장
for i in range(n):
  data.append(int(sys.stdin.readline()))

# 입력된 값들을 내림차순으로 정렬
data.sort(reverse=True)

# 정렬이 수행된 결과 출
for i in data:
  print(i,end=" ")
