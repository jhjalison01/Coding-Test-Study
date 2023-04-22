#배달해야 하는 봉지의 무게
n=int(input())

#봉지 3kg, 5kg
array=[3,5]

#DP 테이블 초기화
d=[5001]*(n+1)
d[0]=0

#다이나믹 프로그래밍 구현(보텀업)
for i in range(2):
  for j in range(i,n+1):
    d[j]=min(d[j],d[j-array[i]]+1)

#결과값 출력
if d[n]==5001:
  print(-1)
else:
  print(d[n])