import sys
input=sys.stdin.readline

#부등호 관계에 만족하는 지 확인
def check(a,b,op):
  if op=='<':
    if a>b: return False
  if op=='>':
    if a<b: return False
  return True

#백트래킹
def sol(cnt,num):
  if cnt==k+1:
    answer.append(num)
    return
  #숫자는 0부터 9까지
  for i in range(10):
    #정수를 사용한 경우
    if visited[i]: continue
    #정수의 길이가 0이거나 부등호 관계에 만족하는 경우
    if cnt==0 or check(num[cnt-1],str(i),op[cnt-1]):
      visited[i]=1
      sol(cnt+1,num+str(i)) #백트래킹 실행
      visited[i]=0

#부등호 개수
k=int(input())
#부등호
op=list(input().split())
visited=[0]*10
answer=[]
#백트래킹 실행
sol(0,"")
#정수 정렬
answer.sort()
#최대,최소 정수 출력
print(answer[-1])
print(answer[0])