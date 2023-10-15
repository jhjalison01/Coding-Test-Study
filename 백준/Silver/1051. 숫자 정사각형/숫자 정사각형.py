import sys
input=sys.stdin.readline
#n,m 입력 받기
n,m=map(int,input().split())
#직사각형 정보 입력 받기
data=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
  a=input()
  for j in range(m):
    data[i][j]=a[j]

#정사각형 한 변 최대 길이
max_len=min(n,m)

#정사각형 네 꼭짓점이 모두 같은 지 확인
def check(s):
  for i in range(n-s+1):
    for j in range(m-s+1):
      x1,y1=i,j #정사각형 꼭짓점 중 하나
      x2,y2=i+s-1, j+s-1 #(x1,y1)에서 가장 먼 점
      #네 꼭짓점의 값이 모두 같을 경우 반복 종료
      if data[x1][y1]==data[x2][y2]==data[x1][y2]==data[x2][y1]:
        return True
  return False

#최대 크기부터 하나씩 줄여가며 확인함
for k in range(max_len,0,-1):
  if check(k):
    print(k**2) #정사각형 크기 출력
    break