import sys
input=sys.stdin.readline

n=int(input()) #사진틀 개수
m=int(input()) #총 추천 횟수
nums=list(map(int,input().split()))
score=[] #추천 수

result=[] #사진틀
for i in range(m):
  #사진틀에 해당 학생이 있는 경우
  if nums[i] in result:
    for j in range(len(result)):
      if nums[i]==result[j]:
        score[j]+=1
  else: #사진틀에 없는 경우
    if len(result)>=n: #사진틀이 꽉 찬 경우
      for j in range(n):
        if score[j] == min(score): #가장 작은 점수 찾기
          del result[j] #사진틀에서 제거
          del score[j] #추천수 리스트에서도 제거
          break
    #사진틀에 추가
    result.append(nums[i])
    score.append(1)

result.sort()
print(*result)