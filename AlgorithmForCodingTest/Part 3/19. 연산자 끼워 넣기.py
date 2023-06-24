#이것이 취업을 위한 코딩 테스트다 Part3 DFS/BFS 19. 연산자 끼워 넣기
#백준 14888

import sys
input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

#최솟값, 최댓값 초기
min_value=int(1e9)
max_value=int(-1e9)

#DFS 구현
def dfs(i,now,add, sub, mul, div):
  global min_value,max_value
  #모든 연산자를 다 사용한 경우 최솟값, 최댓값 업데이트
  if i==n:
    min_value=min(min_value,now)
    max_value=max(max_value,now)
    return
  else:
    #각 연산자에 대해 재귀적으로 수행
    if add>0:
      dfs(i+1,now+data[i],add - 1, sub, mul, div)
    if sub>0:
      dfs(i+1,now-data[i],add, sub-1, mul, div)
    if mul>0:
      dfs(i+1,now*data[i],add, sub, mul-1, div)
    if div>0:
      dfs(i+1,int(now/data[i]),add, sub, mul, div-1) #음수를 양수로 나눌 때 C++14의 기준을 따르기 때문

#dfs 메서드 호출
dfs(1,data[0],add, sub, mul, div)

#최댓값, 최솟값 출력
print(max_value)
print(min_value)
