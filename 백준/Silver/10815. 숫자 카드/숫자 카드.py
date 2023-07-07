import sys
input=sys.stdin.readline

n=int(input()) #상근이가 가지고 있는 숫자 카드 개수
card=list(map(int,input().split())) #상근이의 숫자 카드
m=int(input()) #확인해야 할 카드의 개수
data=list(map(int,input().split())) #확인해야 할 카드

#리스트 사용 시 시간초과가 되므로 딕셔너리 사용
dict={}
for x in card:
  dict[x]=0 #아무 숫자로 mapping

for x in data:
  if x in dict: #해당 카드를 상근이가 가지고 있는 경우 1 출력
    print(1,end=" ") 
  else: #해당 카드를 상근이가 가지고 있지 않는 경우 0 출력
    print(0,end=" ")