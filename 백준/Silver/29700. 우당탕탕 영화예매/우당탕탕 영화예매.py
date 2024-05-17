import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
data=[]
answer=0

for _ in range(n):
  #가로줄 입력 받기
  row=input().rstrip()
  for i in range(m-k+1):
    # i부터 (i+k-1)까지 모두 예매 가능한 경우
    if '1' not in row[i:i+k]:
      answer+=1
      
print(answer)