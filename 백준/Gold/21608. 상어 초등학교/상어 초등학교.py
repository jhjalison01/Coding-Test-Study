import sys
input=sys.stdin.readline
  
N=int(input())
#각 학생이 좋아하는 학생 정보
data=[]
for _ in range(N**2):
  data.append(list(map(int,input().split())))

#교실 배치
room=[[0 for _ in range(N)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N**2):
  student=data[i]
  temp=[]
  for r in range(N):
    for c in range(N):
      if room[r][c]==0: #빈칸일 경우
        like=0
        blank=0
        for k in range(4): #인접한 칸 확인
          nr=r+dx[k]
          nc=c+dy[k]
          if 0<=nr<N and 0<=nc<N:
            if room[nr][nc] in student[1:]: #좋아하는 학생이 앉았을 경우
              like+=1
            if room[nr][nc]==0: #빈칸일 경우
              blank+=1
        temp.append([like,blank,r,c])
  #좋아하는 인접한 칸이 많을 수록, 인접한 칸 중 비어있는 칸이 많을 수록, 행의 번호가 작을 수록, 열의 번호가 작을 수록
  temp.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
  room[temp[0][2]][temp[0][3]]=student[0] #정렬 후 맨 앞에 있는 자리에 학생 앉히기
  
answer=0
data.sort()

for x in range(N):
  for y in range(N):
    total=0
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if 0<=nx<N and 0<=ny<N:
        if room[nx][ny] in data[room[x][y]-1]: #좋아하는 학생이 앉았을 경우
          total+=1
    if total!=0:
      answer+=10**(total-1)

print(answer)