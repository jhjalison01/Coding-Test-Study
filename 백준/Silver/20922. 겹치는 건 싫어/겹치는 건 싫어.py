import sys
input=sys.stdin.readline
from collections import defaultdict

#n: 수열 길이, k:같은 원소가 k개 이하로 들어 있어야 함
n,k=map(int,input().split())
#수열
data=list(map(int,input().split()))
answer=1
#투 포인터
start=0
end=0
#숫자 개수 카운트하는 딕셔너리
dict=defaultdict(int)

while end<n:
  #start가 가리키고 있는 숫자
  start_num=data[start]
  #end가 가리키고 있는 숫자
  end_num=data[end]
  #포함시키려고 하는 숫자가 이미 k개 이상 일 경우
  if dict[end_num]>=k:
    dict[start_num]-=1
    start+=1
  else:
    # end가 가리키는 숫자 포함시키기
    dict[end_num]+=1
    end+=1
    #최장 수열 길이 구하기
    answer=max(answer, end-start)

#최장 연속 수열의 길이 출력
print(answer)