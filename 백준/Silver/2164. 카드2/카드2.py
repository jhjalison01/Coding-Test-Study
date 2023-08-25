from collections import deque
#N 입력받기
n=int(input())
#큐에 1부터 n까지 수 집어넣기
q=deque()
for i in range(1,n+1):
  q.append(i)
#q에 숫자가 하나 남을 때까지 반복
while len(q)>1:
  q.popleft() #맨 아래 카드 버리기
  a=q.popleft()
  q.append(a) #맨 아래 카드 위로 보내기

print(q[0]) #남아 있는 숫자 출력