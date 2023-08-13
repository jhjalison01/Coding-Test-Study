#n,m 입력 받기
n,m=map(int,input().split())
#수열 입력 받기
a=list(map(int,input().split()))

left=0 #왼쪽 포인터
right=1 #오른쪽 포인터
cnt=0 #경우의 수

while left<=right and right<=n:
  #left부터 right-1까지 합 구하기
  total=sum(a[left:right])
  #합이 m일 경우 경우의 수 증가
  if total==m:
    cnt+=1
    right+=1
  #합이 m보다 작을 경우 right를 1 증가시켜 부분합을 늘린다
  elif total<m:
    right+=1
  #합이 m보다 클 경우 left를 1 감소시켜 부분합을 줄인다
  else:
    left+=1
    
print(cnt)