import sys
input=sys.stdin.readline

n=int(input())
rocks=list(map(int,input().split()))
start=int(input())
visited=[0]*n

cnt=1
def dfs(x):
  global cnt
  #오른쪽으로 가는 경우, 왼쪽으로 가는 경우
  for nx in (x+rocks[x],x-rocks[x]):
    #돌다리 안으로 가고 간 적이 없는 경우
    if 0<=nx<n and not visited[nx]:
      cnt+=1
      visited[nx]=1
      dfs(nx)
      
dfs(start-1)    
print(cnt)