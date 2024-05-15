#층수 구하기
def find(num):
  k=0
  while True:
    if 2**k>num:
      break
    else:
      k+=1
  return k

T=int(input())
for i in range(T):
  #현재 송이가 있는 방의 위치
  num=int(input())
  #k층 s번 방
  k=find(num)
  s=(num-2**(k-1))+1
  while k>0:
    print(str(k)+'0'*(18-len(str(s)))+str(s))
    #윗 층으로 올라가기
    k-=1
    s=(s+1)//2