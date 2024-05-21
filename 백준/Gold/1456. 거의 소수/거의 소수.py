import sys
input=sys.stdin.readline

a,b=map(int,input().split())

#소수 리스트
prime=[True]*int((b**0.5)+1)
prime[1]=False

#에라토스테네스의 체를 이용하여 소수가 아닌 것 제외시키기
for i in range(2,int((b**0.5)+1)):
  if prime[i]:
    if i*i>int(b**0.5):
      break
    for j in range(i**2, int(b**0.5)+1,i):
      prime[j]=False

#거의 소수 구하기
cnt=0
for i in range(1,len(prime)):
  #i가 소수일 경우
  if prime[i]:
    temp=i*i
    while True:
      if temp<a:
        temp*=i
        continue
      if temp>b:
        break
      cnt+=1
      temp*=i

print(cnt)