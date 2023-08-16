#n 입력 받기
n=int(input())
#배열 A 입력 받기
data=list(map(int,input().split()))
visited=[False]*n
answer=0

def solve(li):
  global answer
  #li에 정수들을 모두 배열했을 경우 - 결과값 구하기
  if len(li)==n:
    total=0
    for i in range(n-1):
      total+=abs(li[i]-li[i+1])
    answer=max(answer,total)
    return
  
  for i in range(n):
    #해당 정수를 li에 넣지 않았을 경우
    if not visited[i]:
      visited[i]=True
      li.append(data[i])
      #재귀 시작
      solve(li)
      #리턴 후 원래대로 돌려놓기
      visited[i]=False
      li.pop()

#함수 실행
solve([])
print(answer) #최댓값 출력