import sys
input=sys.stdin.readline

#n,m 입력 받기
n,m=map(int,input().split())
#배열 a,b 입력 받기
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#a와 b 합치기
a.extend(b)
#정렬
a.sort()
#정렬한 결과 출력
print(*a)