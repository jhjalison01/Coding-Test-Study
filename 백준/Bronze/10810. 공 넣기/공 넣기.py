import sys
input=sys.stdin.readline

n,m=map(int,input().split())
basket=[0]*(n+1)

#i부터 j까지 num번 번호가 적혀져 있는 공 넣기
for _ in range(m):
  i,j,num=map(int,input().split())
  for x in range(i,j+1):
    basket[x]=num

#1부터 n번 바구니에 들어있는 공의 번호 출력
for i in range(1,n+1):
  print(basket[i],end=" ")