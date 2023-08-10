#응시자 수, 상받는 사람의 수 입력 받기
n,k=map(int,input().split())
#학생의 점수 입력 받기
data=list(map(int,input().split()))
#점수를 내림차순으로 정렬
data.sort(reverse=True)
#커트라인 출력
print(data[k-1])