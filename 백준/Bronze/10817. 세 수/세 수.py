#세 수를 입력 받기
data=list(map(int,input().split()))

#내림차순으로 정렬
data.sort(reverse=True)
print(data[1]) #두 번째로 큰 수 출력