#e,s,m 입력받기
e,s,m=map(int,input().split())

k=1
#구하는 수가 나올 때까지 반복
while True:
  a=k%15 #해당 수를 15로 나눈 수
  b=k%28 #해당 수를 28로 나눈 수
  c=k%19 # 해당 수를 19로 나눈 수
  
  if (a==e or (a==0 and e==15)) and (b==s or (b==0 and s==28)) and (c==m or (c==0 and m==19)):
    print(k) #e,s,m으로 표시되는 가장 빠른 연도 출
    break
  k+=1