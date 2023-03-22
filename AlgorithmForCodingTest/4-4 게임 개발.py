data=[]
result=1

n, m =map(int, input().split())
a, b, d=map(int, input().split())
for i in range(m):
  data.append(list(map(int, input().split())))
  
move_list=[[-1,0],[0,1],[1,0],[0,-1]] #북,동,남,서 순서
data[a][b]=2 #현재 좌표 방문 처리

while True:
  #네 방향 모두 이미 가본 칸 일 때
  if data[a][b+1]!=0 and data[a][b-1]!=0 and data[a+1][b]!=0 and data[a-1][b]!=0:
    if d==0 or d==1:
      #뒤쪽 방향이 바다인 칸일 때
      if data[a+move_list[d+2][0]][b+move_list[d+2][1]]==1:
        break
      #뒤가 바다가 아니면 뒤로 한 칸 가기
      a=a+move_list[d+2][0]
      b=b+move_list[d+2][1]
    elif d==2 or d==3:
      if data[a+move_list[d-2][0]][b+move_list[d-2][1]]==1:
        break
      a=a+move_list[d-2][0]
      b=b+move_list[d-2][1]
    continue
    
  #왼쪽 방향으로 돌리기
  if d==0:
    d=3
  else:
    d-=1
    
  #가본 칸인지 확인
  if data[a+move_list[d][0]][b+move_list[d][1]]!=0:
    continue
  else:
    a=a+move_list[d][0]
    b=b+move_list[d][1]
    data[a][b]=2
    result+=1

print(result)