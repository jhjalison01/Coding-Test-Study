import sys
sys.setrecursionlimit(100000)

#dfs 구현
def dfs(x,y):
  #주어진 범위에서 벗어났다면 즉시 종료
  if x<0 or x>=h or y<0 or y>=w:
    return False
  #해당 섬을 아직 방문하지 않은 경우
  if graph[x][y]==1:
    graph[x][y]=2 #방문 처리
    dfs(x+1,y) #위
    dfs(x-1,y) #아래
    dfs(x,y-1) #왼쪽
    dfs(x,y+1) #오른쪽
    dfs(x-1,y+1) #오른쪽 위
    dfs(x-1,y-1) #왼쪽 위
    dfs(x+1,y+1) #오른쪽 아래
    dfs(x+1,y-1) #왼쪽 아래
    return True
  return False
      
while True:
  w,h=map(int,input().split()) #너비, 높이 입력 받기
  if w==0 and h==0: #w,h 모두 0일 경우 종료
    break
  #지도 정보 입력 받기
  graph=[]
  for i in range(h):
    graph.append(list(map(int,input().split())))
  result=0 #섬의 개수
  for i in range(h):
    for j in range(w):
      #현재 위치에서 dfs 실행
      if graph[i][j]==1:
        if dfs(i,j):
          result+=1
  print(result)