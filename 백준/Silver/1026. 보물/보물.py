#n 입력 받기
n=int(input())
#a,b에 있는 수 입력 받기
a=list(map(int,input().split()))
b=list(map(int,input().split()))

answer=0
#a에서 가장 큰 수와 b에서 가장 작은 수끼리 곱하여 더한다.
for i in range(n):
  answer+=max(a)*min(b)
  a.pop(a.index(max(a)))
  b.pop(b.index(min(b)))

print(answer)