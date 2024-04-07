import sys
input=sys.stdin.readline

# (x,y) : 시작 위치, length: 해당 종이의 한 변의 길이
def sol(x,y,length):
  num=data[x][y]
  #종이가 하나의 정수로 채워져 있는지 확인
  for i in range(x,x+length):
    for j in range(y,y+length):
      #다른 정수가 있을 경우
      if data[i][j] !=num:
        #종이를 9개로 자르고 다시 확인
        for k in range(3):
          for l in range(3):
            #재귀 함수 실행
            sol(x+k*length//3,y+l*length//3,length//3)
        return
  #종이가 하나의 정수로 채워져 있을 경우
  if num==-1:
    answer[0]+=1
  elif num==0:
    answer[1]+=1
  else:
    answer[2]+=1

# 종이 한 변의 길이
n=int(input())
#종이 정보 입력받기
data=[]
for i in range(n):
  data.append(list(map(int,input().split())))

#-1,0,1로만 채워진 종이의 수
answer=[0,0,0]

sol(0,0,n)
#정답 출력
for i in range(3):
  print(answer[i])