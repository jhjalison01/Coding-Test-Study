#이것이 취업을 위한 코딩 테스트다 Chapter 8 다이나믹 프로그래밍 실전문제4 <효율적인 화폐 구성>
import sys

#N(화폐 종류),M(화폐 가치의 합) 입력 받기
n,m = map(int,sys.stdin.readline().split())

#화폐의 가치 입력 받기
money=[]
for i in range(n):
  money.append(int(sys.stdin.readline().rstrip()))

#DP 테이블 초기화
d=[10001]*(m+1)
d[0]=0 #화폐 가치 합이 0일 때 필요한 화폐 개수는 0개

#다이나믹 프로그래밍 구현(보텀업)
#금액 i를 만들 수 있는 최소한의 화폐 개수를 a(i), 화폐 단위를 k, 금액(i-k)를 만들 수 있는 최소한의 화폐 개수를 a(i-k)라고 하면
#a(i)=min(a(i), a(i-k)+1)
for i in range(n):
  for j in range(money[i],m+1):
    d[j]=min(d[j],d[j-money[i]]+1)

#값이 10001이면 합을 만들 수 없다는 뜻이므로 -1을 출력
if d[m]==10001:
  print(-1)
else:
  print(d[m]) #합을 만들 수 있다면 계산된 결과를 출력
