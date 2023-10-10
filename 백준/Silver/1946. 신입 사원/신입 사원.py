import sys
input=sys.stdin.readline

#테스트 케이스 개수
case=int(input())
for i in range(case):
  #지원자 수
  n=int(input())
  #지원자 서류,면접 순위
  rank=[]
  for j in range(n):
    rank.append(list(map(int,input().split())))
  #서류 순위를 기준으로 정렬 
  rank.sort()
  result=1 #서류 순위에서 1위한 지원자 포함
  top=rank[0][1] #서류 순위 1위한 지원자의 면접 순위
  for j in range(1,n):
    if rank[j][1]<top: #면접 순위가 더 높을 경우
      top=rank[j][1]
      result+=1
  print(result)