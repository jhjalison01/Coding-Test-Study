import itertools
#숫자 N 입력 받기
n=int(input())
#1부터 N까지 리스트 만들기
data=list(range(1,n+1))
#순열 구하기
for x in itertools.permutations(data,n):
  print(*x) #튜플의 요소를 공백으로 구분하여 출력