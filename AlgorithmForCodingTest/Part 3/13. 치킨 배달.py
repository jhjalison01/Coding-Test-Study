import itertools

n,m=map(int, input().split())
data=[] #도시 맵
chicken=[] #치킨집 위치
house=[] #집 위치
INF=int(1e9)
answer=INF

for i in range(n):
  #도시 맵 입력 받기
  data.append(list(map(int,input().split())))
  #치킨집과 집 위치 확인하기
  for j in range(n):
    if data[i][j]==2:
      chicken.append([i,j])
    elif data[i][j]==1:
      house.append([i,j])

#폐업시키지 않을 치킨집 m개를 뽑는 경우의 수 구하기
combination=list(itertools.combinations(chicken, m))

#모든 경우의 수에 대한 도시의 치킨 거리를 구함
for x in combination:
  temp=0 #해당 경우의 수에 대한 도시의 치킨 거리
  for h in house:
    distance=n*2
    for y in x:
      distance=min(distance,abs(h[0]-y[0])+abs(h[1]-y[1])) #해당 집의 치킨 거리 구하기
    temp+=distance
  answer=min(answer,temp)

print(answer)
