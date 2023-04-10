#이것이 취업을 위한 코딩 테스트다 Chapter6 정렬 실전문제3
import sys

n=int(sys.stdin.readline())

data=[]
#학생 정보를 리스트에 저장
for i in range(n):
  input_data=sys.stdin.readline().split()
  data.append((input_data[0],int(input_data[1])))

# key를 이용하여 점수를 기준으로 오름차순으로 정렬
data=sorted(data, key=lambda x: x[1])

#결과 출력
for i in data:
  print(i[0], end=" ")
