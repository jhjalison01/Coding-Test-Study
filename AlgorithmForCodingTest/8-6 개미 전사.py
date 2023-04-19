#이것이 취업을 위한 코딩 테스트다 Chapter 8 다이나믹 프로그래밍 실전문제3 <개미 전사>
import sys

#식량 창고 개수 N 입력 받기
n=int(sys.stdin.readline().rstrip())
#각 식량 창고에 저장된 식량의 개수 입력 받기
data=list(map(int,sys.stdin.readline().split()))

d=[0]*n #앞서 계산된 결과를 저장하기 위해 DP 테이블 초기화

d[0]=data[0] #식량창고가 1개 있을 때 식량의 최댓값 대입
d[1]=max(data[0],data[1]) #식량 창고가 2개 있을 때 식량의 최댓값 대입

#다이나믹 프로그램 구현(보텀업)
for i in range(2,n):
  #(i-1)번째 식량창고를 턴다면 i번째를 털 수 없고 (i-2)번째를 턴다면 i번째를 털 수 있다.
  #(i-1)번째를 털 때의 최댓과 (i-2)번째를 털 때의 최댓값에 현재 식량 창고의 식량 개수를 더한 값 중 큰 값을 대입한다.
  d[i]=max(d[i-1], d[i-2]+data[i])

print(d[i])
