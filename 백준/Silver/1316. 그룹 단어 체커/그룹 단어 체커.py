n=int(input())
answer=n

for _ in range(n):
  word=input()
  data=[word[0]]
  for i in range(1,len(word)):
    #해당 문자가 떨어져 나타났을 경우 그룹 단어가 아님
    if data[-1]!=word[i] and word[i] in data:
      answer-=1
      break
    data.append(word[i]) #해당 문자 넣기

print(answer)    