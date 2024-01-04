import sys
input=sys.stdin.readline

n=int(input()) #노드 개수
data=list(map(int,input().split())) #각 노드의 부모
erase=int(input()) #지울 노드 번호

def dfs(num,data):
  data[num]=-2 #노드 삭제
  for i in range(n):
    if data[i]==num: #삭제되는 노드가 현재 노드의 부모일 경우
      dfs(i,data) #재귀 호출

dfs(erase,data)
cnt=0
for i in range(n):
  #i를 부모로 가진 노드가 없고 i 노드가 삭제가 안 됐을 경우
  if data[i]!=-2 and i not in data:
    cnt+=1

print(cnt)