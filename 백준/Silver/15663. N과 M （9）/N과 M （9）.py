import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nums=sorted(list(map(int,input().split())))
visited=[0]*n
temp=[]

def dfs():
  if len(temp)==m:
    print(*temp)
    return
  check=0
  for i in range(n):
    #중복된 수열을 중복으로 여러 번 출력하면 안 되므로
    if not visited[i] and check!=nums[i]:
      visited[i]=1
      temp.append(nums[i])
      check=nums[i]
      dfs()
      visited[i]=0
      temp.pop()

dfs()