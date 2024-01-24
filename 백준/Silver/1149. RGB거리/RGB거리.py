import sys
input=sys.stdin.readline

# n 입력 받기
n=int(input())

#각 집을 칠하는 비용 입력 받기
cost=[]
for i in range(n):
  cost.append(list(map(int,input().split())))

# 이전 비용 중 현재 집 색깔과 다른 색깔로 칠할 때의 최소 비용 구하기
for i in range(1,n):
  cost[i][0]+=min(cost[i-1][1],cost[i-1][2])
  cost[i][1]+=min(cost[i-1][0],cost[i-1][2])
  cost[i][2]+=min(cost[i-1][0],cost[i-1][1])

#집 칠하는 비용의 최솟값 출력
print(min(cost[-1]))