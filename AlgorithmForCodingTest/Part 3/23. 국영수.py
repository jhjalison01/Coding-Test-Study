#이것이 취업을 위한 코딩 테스트다 Part3 정렬 23. 국영수
#백준 10825

n=int(input())
data=[]

#학생 성적 입력 받기
for i in range(n):
  data.append(input().split())

#정렬 기준에 따라 정렬
data.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

#정렬된 학생 이름만 출력
for i in range(n):
  print(data[i][0])
