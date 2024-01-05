import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

#전위 순회: 루트 - 왼쪽 - 오른쪽 이므로 루트보다 큰 값이 나오는 노드부터가 오른쪽 서브 트리이고 그 전은 왼쪽 서브 트리이다.
#루트보다 큰 노드를 찾아 왼쪽, 오른쪽으로 나누어 재귀를 한다.

#트리 정보 입력 받기
data=[]
while True:
  try:
    data.append(int(input()))
  except:
    break

#후위 순회
def post(start,end):
  if start>end:
    return
  mid=end+1 #모든 노드가 루트보다 작을 수도 있으므로 end+1로 초기화
  #루트보다 큰 노드 찾기
  for i in range(start+1,end+1):
    if data[i]>data[start]:
      mid=i
      break

  post(start+1,mid-1) #왼쪽 노드
  post(mid,end) #오른쪽 노드
  print(data[start]) #루트 노드

post(0,len(data)-1)