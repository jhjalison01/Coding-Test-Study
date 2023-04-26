#이것이 취업을 위한 코딩 테스트다 part3 그리디 2. 곱하기 혹은 더하기
n=input() #문자열 입력 받기

left=int(n[0]) #처음 숫자 대입

for i in range(1, len(n)):
  num=int(n[i])
  if num<=1 or left<=1: # 두 수 중 하나라도 0이거나 1이면 더하기를 수행
    left+=num
  else:
    left*=num

print(left) #결과값 출력
