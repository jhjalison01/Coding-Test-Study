#이것이 취업을 위한 코딩 테스트다 Part3 이진 탐색 29. 공유기 설치

#mid - 가장 인접한 두 공유기 사이의 거리
#처음 mid의 값은 최소 거리와 최대 거리의 중앙값이 된다.
import sys
input=sys.stdin.readline

n,c=map(int, input().split())
houses=[]

for i in range(n):
  houses.append(int(input()))
houses.sort() #이진 탐색을 위해 정렬

start=1 #가능한 최소 거리
end=houses[n-1]-houses[0] #가능한 최대 거리
answer=0

while start<=end:
  mid=(start+end)//2
  value=houses[0] #마지막으로 설치된 공유기의 위치
  count=1#설치한 공유기 개수
  for i in range(1,n):
    #가장 인접한 두 공유기 사이의 거리의 최댓값을 구하는 것이므로 공유기 사이의 거리가 mid보다 크거나 같을 때 공유기를 설치한다.
    if houses[i]-value>=mid:
      value=houses[i]
      count+=1
  if count>=c: #c개 이상의 공유기를 모두 설치할 수 있는 경우, 거리를 증가
    start=mid+1
    answer=mid
  else: #c개 이상의 공유기를 모두 설치할 수 없는 경우, 거리 감소
    end=mid-1

print(answer)
