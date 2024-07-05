import sys
input=sys.stdin.readline

n,m=map(int,input().split())

def dfs(num):
  if len(num) == m:
    print(*num)
    return

  for i in range(1,n+1):
    if i not in num:
      num.append(i)
      dfs(num)
      num.pop()

dfs([])