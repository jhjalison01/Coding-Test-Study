import sys
input=sys.stdin.readline

k,n=map(int,input().split())

lan=[]
for i in range(k):
  lan.append(int(input()))

start,end=1,max(lan)
#이진 탐색 실행
while start<=end:
  mid=(start+end)//2
  lines=0
  for l in lan:
    lines+=l//mid
  if lines>=n: #n개의 랜선을 만들 수 있는 경우
    start=mid+1
  else: #n개의 랜선을 만들 수 없는 경우
    end=mid-1

print(end)
