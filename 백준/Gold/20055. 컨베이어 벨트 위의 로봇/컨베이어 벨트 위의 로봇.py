from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
belt=deque(map(int,input().split())) #0~(n-1), n~(2n-1)
robot=deque([False]*n)
answer=0 #단계 카운트

while True:
  answer+=1 #한 단계 실행
  #벨트 한 칸 회전
  belt.rotate(1)
  robot.rotate(1)
  robot[-1]=False #로봇 내려가는 곳이므로
  if True in robot:
    #먼저 벨트에 올라간 로봇부터 한 칸 이동
    for i in range(n-2,-1,-1):
      #해당 칸에 로봇이 있고 다음 칸에 로봇이 없고 다음칸 내구성이 1 이상일 경우
      if robot[i]==True and robot[i+1]==False and belt[i+1]>=1:
        robot[i]=False
        robot[i+1]=True
        belt[i+1]-=1
    robot[-1]=False #로봇 내려가는 곳이므로
  #올리는 위치 칸의 내구도가 0이 아닌 경우 로봇 올림
  if belt[0]!=0:
    robot[0]=True
    belt[0]-=1
  #내구도가 0인 칸의 개수가 k개 이상일 경우 종료
  if belt.count(0)>=k:
    break
  
print(answer) #정답 출력