import sys
input=sys.stdin.readline

n,m=map(int,input().split())
#수열 입력 받기
data=[]
for _ in range(n):
  data.append(int(input()))
data.sort() #투 포인터 사용을 위해 정렬

left,right=0,0 #투 포인터
answer=int(1e11) #정답

while left<=right and right<n:
  #두 정수의 차이가 m 미만일 경우
  if data[right]-data[left]<m:
    right+=1 #차이를 증가시키기 위해 right를 오른쪽을 옮기기
  else:
    answer=min(answer, data[right]-data[left])
    left+=1 #차이를 줄이기 위해 left를 오른쪽으로 옮기기

#m 이상이면서 제일 작은 차이 출력
print(answer)