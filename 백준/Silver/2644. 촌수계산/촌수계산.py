import sys
input=sys.stdin.readline
from collections import deque

#전체 사람의 수
n=int(input())
#촌수를 계산해야 하는 서로 다른 두 사람의 번호
a,b=map(int,input().split())
#부모 자식들 간의 관계의 개수
m=int(input())
#부모 자식간의 관계
rel=[[] for _ in range(n+1)]
for _ in range(m):
  #x: y의 부모 번호
  x,y=map(int,input().split())
  rel[x].append(y)
  rel[y].append(x)

#촌수 카운트
cnt=[0 for _ in range(n+1)]

#bfs 구현
def bfs(x):
  q=deque()
  q.append(x)
  while q:
    now=q.popleft()
    for i in rel[now]:
      if cnt[i]==0:
        #촌수 카운트
        cnt[i]=cnt[now]+1
        q.append(i)

bfs(a)
#두 사람의 친척 관계까 전혀 없을 경우
if cnt[b]==0:
  print(-1)
else:
  print(cnt[b])