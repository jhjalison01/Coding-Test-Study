import sys
input=sys.stdin.readline

n=int(input())

#책 제목 입력 받기
data={}
for i in range(n):
  a=input().rstrip()
  if a in data:
    data[a]+=1
  else:
    data[a]=1

#사전 순으로 정렬
data=dict(sorted(data.items()))
#가장 많이 팔린 순으로 정렬
data=sorted(data.items(),key=lambda x: x[1],reverse=True)

#가장 많이 팔린 책 제목 출력
print(data[0][0])