#이것이 취업을 위한 코딩 테스트다 Part3 정렬 24. 안테나
#백준 18310번

#중간값에 해당되는 위치의 집에 안테나를 설치했을 때 안테나로부터 모든 집까지의 거리의 총합이 최소가 된디.

import sys
input = sys.stdin.readline

n=int(input())
houses=list(map(int,input().split()))

houses.sort()

#중간값 출력
print(houses[(n-1)//2])
