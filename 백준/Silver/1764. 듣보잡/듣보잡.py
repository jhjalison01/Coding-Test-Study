#n,m 입력 받기
n,m=map(int,input().split())

#듣도 못한 사람, 보도 못한 사람 입력받기
no_hear=set()
no_see=set()
for i in range(n):
  no_hear.add(input())

for i in range(m):
  no_see.add(input())

#두 집합의 교집합 구하기
data=list(no_hear&no_see)
#듣보잡의 수 출력
print(len(data))
#듣보잡 명단 출력
data.sort()
for a in data:
  print(a)