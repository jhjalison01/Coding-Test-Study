import sys
input=sys.stdin.readline

#N까지 숫자를 세웠을 때 입력값에 있는 모든 숫자가 존재해야한다. 

num=input().rstrip()
n=0
idx=0

while True:
  n+=1
  for s in str(n):
    if num[idx]==s:
      idx+=1
      if idx>=len(num):
        print(n)
        exit()