#백트래킹 구현
def solve(idx,cnt):
  #길이가 6이 되었을 때 리턴
  if cnt==6:
    print(*result)
    return
  
  for i in range(idx,k):
    result.append(data[i])
    solve(i+1,cnt+1)
    result.pop()
    

while True:
  data=list(map(int,input().split()))
  k=data[0]
  data=data[1:]
  #0이 나올 때까지 반복
  if k==0:
    break
  result=[]
  solve(0,0)
  print()