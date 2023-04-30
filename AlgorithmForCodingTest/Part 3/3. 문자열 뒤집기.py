#이것이 취업을 위한 코딩 테스트다 Part3 그리디 3. 문자열 뒤집기
s=input()

count0=0 #0으로 바꿀 때 횟수
count1=0 #1로 바꿀 때 횟수

#첫 번째 원소 처리
if s[0]=='1':
  count0+=1
else:
  count1+=1

#두 번째 원소부터 모든 원소를 확인
for i in range(len(s)-1):
  if s[i]!=s[i+1]: #다음 원소가 현재 원소와 다를 때
    if s[i+1]=='1': #다음 원소가 1일 때
      count0+=1
    else: #다음 원소가 0일 때
      count1+=1

print(min(count0,count1)) #둘 중 작은 수를 출력
