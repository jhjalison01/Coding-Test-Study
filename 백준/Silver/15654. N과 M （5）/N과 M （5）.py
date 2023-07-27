#n,m 입력 받기
n,m=map(int, input().split())
#숫자 입력 받기
data=list(map(int,input().split()))
#숫자 오름차순으로 정렬
data.sort()
result=[]
#백트래킹 구현
def solve(cnt):
  #숫자를 m만큼 선택했을 경우 결과 출력, 리턴
  if cnt==m:
    print(" ".join(map(str,result)))
    return
  for i in range(n):
    #data[i]를 아직 선택하지 않은 경우
    if data[i] not in result:
      #result에 숫자 추가
      result.append(data[i])
      #백트래킹 실행
      solve(cnt+1)
      #result에 넣은 숫자 제
      result.pop()

solve(0)