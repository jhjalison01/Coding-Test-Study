import sys
input=sys.stdin.readline

n,m=map(int,input().split())

#딕셔너리에 key로 번호와 포켓몬 이름을 넣고 value로 각각 이름과 번호 저장
dict={}
for i in range(1,n+1):
  a=input().rstrip()
  dict[i]=a
  dict[a]=i

for i in range(m):
  a=input().rstrip()
  if a.isdigit(): #입력한 값이 숫자일 경우
    print(dict[int(a)])
  else: #입력한 값이 포켓몬 이름일 경우
    print(dict[a])