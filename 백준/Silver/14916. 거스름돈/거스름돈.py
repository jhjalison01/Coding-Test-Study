import sys
input=sys.stdin.readline


n=int(input())
cnt=0
while True:
  #5의 배수일 경우
  if n%5==0:
    cnt+=n//5
    break
  else: #5의 배수가 아닐 경우 2씩 빼기
    n-=2
    cnt+=1

  if n<0:
    break

if n<0:
  print(-1)
else:
  print(cnt)