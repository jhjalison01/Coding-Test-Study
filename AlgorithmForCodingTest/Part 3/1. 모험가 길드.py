#이것이 취업을 위한 코딩 테스트다 Part 3(그리디) 1번 모험가 길드
n=int(input()) #모험가의 수
data=list(map(int, input().split())) # 각 모험가의 공포도 값

data.sort() #오름차순으로 정렬

result=0 #총 그룹의 수
count=0 #한 그룹당 모험가의 수

for i in data:
  count+=1 #현재 그룹에 해당 모험가 포함시키기
  if count>=i: #현재 그룹에 모함된 모험가 수가 현재의 공포도 이상이면 그룹이 만들어진다.
    result+=1 #그룹 수 증가시키기
    count=0 #현재 그룹 수 초기화

print(result) # 총 그룹의 수 출력
