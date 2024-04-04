n=int(input())
start=0
end=n

#이진 탐색
while start<=end:
  #중간 지점
  mid=(start+end)//2
  if mid**2<n:
    start=mid+1
  else:
    end=mid-1

print(start)