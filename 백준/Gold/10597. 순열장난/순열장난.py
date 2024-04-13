import sys
input=sys.stdin.readline

nums=input().rstrip()
#n: 숫자 개수
if len(nums)<10:
  n=len(nums)
else:
  n=9+(len(nums)-9)//2

visited=[False for _ in range(n+1)]

def dfs(idx,arr):
  #다 구한 경우 복구된 수열 출력
  if idx==len(nums):
    print(*arr)
    exit()

  #한 자릿수 체크
  num1 = int(nums[idx])
  if not visited[num1]:
    visited[num1]=True
    arr.append(num1)
    dfs(idx+1,arr)
    visited[num1] = False
    arr.pop()
    
  #두 자릿수 체크
  if idx+1<len(nums):
    num2 = int(nums[idx:idx+2])
    if num2<=n and not visited[num2]:
      visited[num2]=True
      arr.append(num2)
      dfs(idx+2,arr)
      visited[num2]=False
      arr.pop()

dfs(0,[])