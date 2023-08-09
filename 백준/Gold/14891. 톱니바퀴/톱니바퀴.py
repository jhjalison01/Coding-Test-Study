from collections import deque

#오른쪽 바퀴 확인
def right(num,d):
  if num>4 or wheel[num-1][2]==wheel[num][6]:
    return
  #해당 바퀴가 왼쪽 바퀴와 극이 다를 경우 회전시킨다
  if wheel[num-1][2]!=wheel[num][6]:
    right(num+1,-d)
    wheel[num].rotate(d)
#왼쪽 바퀴 확인
def left(num,d):
  if num<1 or wheel[num][2]==wheel[num+1][6]:
    return
  #해당 바퀴가 오른쪽 바퀴와 극이 다를 경우 회전시킨다
  if wheel[num][2]!=wheel[num+1][6]:
    left(num-1,-d)
    wheel[num].rotate(d)

wheel = [deque([]) for _ in range(5)]
for i in range(1,5):
  wheel[i]=deque(list(map(int,input())))

k=int(input()) #회전 횟수
for i in range(k):
  num,d=map(int,input().split())
  right(num+1,-d)
  left(num-1,-d)
  #해당 숫자의 수레바퀴 회전
  wheel[num].rotate(d)

answer=0
#n일 경우 0점, s극일 경우 2의 i승 만큼 더함
for i in range(4):
  answer+=wheel[i+1][0]*(2**i)

print(answer)