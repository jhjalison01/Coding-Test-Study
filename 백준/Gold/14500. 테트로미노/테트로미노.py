#풀이
#민트색과 노란색은 따로 계산
#주황,녹색,분홍 테트로미노를 놓는 경우 3x2 또는 2x3의 총합에서 정사각형 2개의 값 뺀다.

#n,m 입력 받기
n,m=map(int,input().split())
#종이 정보 입력 받기
data=[]
for i in range(n):
  data.append(list(map(int, input().split())))

answer=0

for i in range(n):
  for j in range(m):
    #민트 가로로 길게(1x4)
    if j+3<=m-1:
      answer=max(answer,data[i][j]+data[i][j+1]+data[i][j+2]+data[i][j+3])
    #민트 세로로 길게(4x1)
    if i+3<=n-1:
      answer=max(answer,data[i][j]+data[i+1][j]+data[i+2][j]+data[i+3][j])
    #노란색(2x2)
    if i+1<=n-1 and j+1<=m-1:
      answer=max(answer,data[i][j]+data[i+1][j]+data[i][j+1]+data[i+1][j+1])
    #6개씩 가로로 길게(2x3)
    if i+1<=n-1 and j+2<=m-1:
      tmp=data[i][j]+data[i][j+1]+data[i][j+2]+data[i+1][j]+data[i+1][j+1]+data[i+1][j+2]
      #분홍(ㅗ,ㅜ)
      answer=max(answer,tmp-(data[i][j]+data[i][j+2]),tmp-(data[i+1][j]+data[i+1][j+2]))
      #초록
      answer=max(answer,tmp-(data[i][j]+data[i+1][j+2]),tmp-(data[i][j+2]+data[i+1][j]))
      #주황
      answer=max(answer,tmp-(data[i][j]+data[i][j+1]),tmp-(data[i][j+1]+data[i][j+2]),tmp-(data[i+1][j]+data[i+1][j+1]),tmp-(data[i+1][j+1]+data[i+1][j+2]))
      #6개씩 세로로 길게(3x2)
    if i+2<=n-1 and j+1<=m-1:
      tmp=data[i][j]+data[i][j+1]+data[i+1][j]+data[i+1][j+1]+data[i+2][j]+data[i+2][j+1]
      #분홍(ㅓ,ㅏ)
      answer=max(answer,tmp-(data[i][j]+data[i+2][j]),tmp-(data[i][j+1]+data[i+2][j+1]))
      #초록
      answer=max(answer,tmp-(data[i][j]+data[i+2][j+1]),tmp-(data[i][j+1]+data[i+2][j]))
      #주황
      answer=max(answer,tmp-(data[i][j]+data[i+1][j]),tmp-(data[i+1][j]+data[i+2][j]),tmp-(data[i][j+1]+data[i+1][j+1]),tmp-(data[i+1][j+1]+data[i+2][j+1]))
  
print(answer)