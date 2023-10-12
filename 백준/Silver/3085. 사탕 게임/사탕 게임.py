import sys
input=sys.stdin.readline

#N 입력 받기
N=int(input())
#보드 정보 입력 받기
graph=[list(input()) for _ in range(N)]

def check(graph):
  max_cnt=1
  #열 순회하면서 연속된 숫자 세기
  for i in range(N):
    cnt=1
    for j in range(1,N):
      if graph[i][j] == graph[i][j-1]:
        cnt += 1
      else:
        cnt=1
      max_cnt=max(max_cnt,cnt)
    #행 순회하면서 연속된 숫자 세기
    cnt = 1
    for j in range(1, N):
      if graph[j][i] == graph[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      max_cnt = max(max_cnt, cnt)
  return max_cnt

result=0
for i in range(N):
  for j in range(N):
    #열 바꾸기
    if j+1<N:
      #인접한 것끼리 바꾸기
      graph[i][j],graph[i][j+1]=graph[i][j+1],graph[i][j]
      cnt=check(graph)
      result=max(result,cnt)
      #바꾼 것 원래대로 돌려놓기
      graph[i][j],graph[i][j+1]=graph[i][j+1],graph[i][j]
    #행 바꾸기
    if i+1<N:
      #인접한 것끼리 바꾸기
      graph[i][j],graph[i+1][j]=graph[i+1][j],graph[i][j]
      cnt=check(graph)
      result=max(result,cnt)
      #바꾼 것 원래대로 돌려놓기
      graph[i][j],graph[i+1][j]=graph[i+1][j],graph[i][j]

print(result)