import sys
input=sys.stdin.readline
#난쟁이 키 입력 받기
data=[]
for _ in range(9):
  data.append(int(input()))

total=sum(data)
data.sort() #오름차순으로 정렬

for i in range(len(data)):
  for j in range(i+1,len(data)):
    #2명 키를 뺀 값이 100일 경우
    if total-data[i]-data[j]==100:
      for k in range(9):
        if k==i or k==j:
          continue
        print(data[k]) #난쟁이 키 출력
      exit()