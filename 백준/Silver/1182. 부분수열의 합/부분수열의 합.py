import sys
input=sys.stdin.readline

n,s=map(int,input().split())
data=list(map(int,input().split()))
cnt=0

def sol(idx,sum):
  global cnt

  if idx>=n:
    return
    
  sum+=data[idx]
  if sum==s:
    cnt+=1
    
  #현재 data[idx]를 선택한 경우
  sol(idx+1,sum)
  #현재 data[idx]를 선택하지 않은 경우
  sol(idx+1,sum-data[idx])

sol(0,0)
print(cnt)