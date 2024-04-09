import sys
input=sys.stdin.readline

#현재 총 길이, 가운데 길이, 구하려는 순서
def sol(total_length, mid_length, n):
  if n<=3:
    return "moo"[n-1]
  
  side_length = (total_length - mid_length) //2
  #찾으려는 문자가 왼쪽 수열에 있을 경우
  if n<=side_length:
    return sol(side_length, mid_length-1, n)
  #찾으려는 문자가 오른쪽 수열에 있을 경우
  if n>side_length+mid_length:
    return sol(side_length, mid_length-1, n-side_length - mid_length)
  #찾으려는 문자가 가운데 수열에 있을 경우
  #찾으려는 문자가 가운데 수열의 첫번째면 m, 아닐 경우 0
  if n-side_length==1:
    return "m"
  else:
    return "o"

n=int(input())

total_length = 3
k=0 #몇 번째 수열인지
while total_length<n:
  k+=1
  total_length=2*total_length+k+3

print(sol(total_length, k+3, n))