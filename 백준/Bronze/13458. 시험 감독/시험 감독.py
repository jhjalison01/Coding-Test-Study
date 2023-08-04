import sys
input=sys.stdin.readline
#시험장 개수 입력 받기
n=int(input())
#각 시험장에 있는 응시자의 수 입력받기
people=list(map(int, input().split()))
#총감독관, 부감독관이 감시할 수 있는 응시자의 수
b,c=map(int, input().split())
#총감독관으로 초기화
answer=n
#한 시험장 당 응시자수 확인
for i in range(n):
  #총감독관이 응시자를 모두 감시할 수 없는 경우
  if people[i]>b:
    people[i]-=b
    #부감독관 수 구하기
    cnt=people[i]//c
    if people[i]%c!=0:
      cnt+=1
    answer+=cnt

print(answer)