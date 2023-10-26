import sys
input=sys.stdin.readline
  
#격자 크기, 파이어볼 개수, 이동 횟수
N,M,K=map(int,input().split())
#(r,c)-위치, m-파이어볼 개수, s-속력, d-방향
fireballs=[]
for i in range(M):
  r,c,m,s,d=map(int,input().split())
  fireballs.append([r-1,c-1,m,s,d])

graph=[[[] for _ in range(N)] for _ in range(N)]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

for _ in range(K):
  #파이어볼 이동
  while fireballs:
    r,c,m,s,d=fireballs.pop(0)
    nr=(r+dx[d]*s)%N
    nc=(c+dy[d]*s)%N
    graph[nr][nc].append([m,s,d])
  #이동 후
  for r in range(N):
    for c in range(N):
      #파이어볼이 2개 이상 있는 지 확인
      if len(graph[r][c])>1:
        sum_m,sum_s,d_odd,d_even,cnt=0,0,0,0,len(graph[r][c])
        while graph[r][c]:
          m,s,d=graph[r][c].pop(0)
          sum_m+=m #총질량
          sum_s+=s #총속력
          if d%2==0: #짝수 방향일 경우
            d_even+=1
          else: #홀수 방향일 경우
            d_odd+=1
        if d_odd==cnt or d_even==cnt: #방향이 모두 짝수이거나 홀수일 경우
          nd=[0,2,4,6]
        else:
          nd=[1,3,5,7]
        if sum_m//5!=0: #질량이 0인 파이어볼은 소멸됨
          for d in nd:
            fireballs.append([r,c,sum_m//5,sum_s//cnt,d]) #새로운 파이어볼 저장
      #파이어볼이 1개 있을 경우
      if len(graph[r][c])==1:
        fireballs.append([r,c]+graph[r][c].pop())

#남아있는 파이어볼 질량의 합 출력
print(sum([f[2] for f in fireballs]))