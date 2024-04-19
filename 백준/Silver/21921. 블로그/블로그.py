import sys
input=sys.stdin.readline

n,x = map(int,input().split())
visitors=list(map(int,input().split()))

if max(visitors)==0:
  print("SAD")
else:
  tmp=sum(visitors[:x])
  max_v=tmp
  cnt=1
  for i in range(x,n):
    #왼쪽 끝값 빼기
    tmp-=visitors[i-x]
    #오른쪽 끝값 오른쪽에 있는 값 더하기
    tmp+=visitors[i]
    if max_v<tmp:
      max_v=tmp #최대 방문자 수 갱신
      cnt=1 #기간 개수 갱신
    elif max_v==tmp:
      cnt+=1
  print(max_v)
  print(cnt)