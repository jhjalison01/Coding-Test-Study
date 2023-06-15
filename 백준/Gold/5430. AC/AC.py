from collections import deque
import sys
input=sys.stdin.readline

T=int(input()) #테스트 케이스 개수

for i in range(T):
  p=list(input().rstrip()) # 수행할 함수
  n=int(input()) #배열에 들어있는 수 개수
  arr=deque(eval(input())) #배열을 deque로 바꿈 -> 첫 번째 수를 쉽게 버리기 위해

  flag=0 #R의 개수 카운트

  for x in p:
    if x=='R': #R일 경우 배열 뒤집기
      flag+=1
    else: #D일 경우
      if len(arr)==0:
        print("error")
        arr=['0']
        break
      else:
        if flag%2==0: #R이 짝수 개일 경우
          arr.popleft()
        else: #R이 홀수 개일 경우
          arr.pop()

  if flag%2!=0:
    arr.reverse()
  arr=[str(x) for x in arr]
  if arr!=['0']:
    print("[" + ",".join(arr) + "]")