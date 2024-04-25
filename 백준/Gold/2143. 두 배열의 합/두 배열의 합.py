import sys
input=sys.stdin.readline
import bisect

T = int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

#배열 a,b의 부 배열의 합 모든 경우 구하기
a_sum,b_sum=[],[]
for i in range(n):
  for j in range(i+1,n+1):
    a_sum.append(sum(a[i:j]))
    
for i in range(m):
  for j in range(i+1,m+1):
    b_sum.append(sum(b[i:j]))

#이분 탐색을 위해 정렬
a_sum.sort()
b_sum.sort()

answer=0
for i in range(len(a_sum)):
  tmp=T-a_sum[i]
  left = bisect.bisect_left(b_sum, tmp)
  right = bisect.bisect_right(b_sum, tmp)
  answer+=right-left #경우의 수 추가

print(answer)