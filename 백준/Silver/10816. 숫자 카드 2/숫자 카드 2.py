import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
m=int(input())
sanggun=list(map(int,input().split()))

cnt={}
for i in nums:
    if i in cnt:
      cnt[i]+=1
    else:
      cnt[i]=1

for i in sanggun:
  if i in cnt:
    print(cnt[i],end=" ")
  else:
    print(0,end=" ")