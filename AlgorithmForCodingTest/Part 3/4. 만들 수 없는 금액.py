#이것이 취업을 위한 코딩 테스트다 Part3 그리디 4. 만들 수 없는 금액

#1부터 차례대로 특정한 금액을 만들 수 있는지 확인한다.
# ex) [1,2,3,5,13]이 주어졌다고 할 때
# 1 -> 1을 만들 수 있음
# 1,2 -> 3까지 만들 수 있음
# 1,2,3 -> 6까지 만들 수 있음
# 1,2,3,5 -> 11까지 만들 수 있음
# 12는 만들 지 못함

n=int(input()) #동전 개수 입력 받기

data=list(map(int,input().split())) #동전 입력 받기
data.sort() #오름차순으로 정렬

target=1 #target 값을 동전으로 만들 수 있는지 확인한다.

for x in data:
  if target<x:
    break
  else:
    target+=x

print(target) #만들 수 없는 최소 금액 출력
