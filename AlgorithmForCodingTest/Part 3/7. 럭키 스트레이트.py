#이것이 취업을 위한 코딩 테스트다 Part3 구현 7. 럭키 스트레이트

n=input()

left=list(n[:len(n)//2]) #왼쪽 부분의 요소들
right=list(n[len(n)//2:]) #오른쪽 부분의 요소들

sum_left=0
sum_right=0

for i in left:
  sum_left+=int(i) #왼쪽 부분의 자릿수 합

for i in right:
  sum_right+=int(i) #오른쪽 부분의 자릿수 합

#왼쪽 부분의 자릿수 합과 오른쪽 부분의 자릿수 합이 같은 지 확인
if sum_left==sum_right:
  print("LUCKY")
else:
  print("READY")
