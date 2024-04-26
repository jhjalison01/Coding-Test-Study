import sys
input=sys.stdin.readline

n,m=map(int,input().split())

words={}
for _ in range(n):
  word=input().rstrip()
  #m보다 짧은 단어는 포함하지 않음
  if len(word)<m :
    continue
  else:
    #단어 개수 카운트
    if word in words:
      words[word]+=1
    else:
      words[word]=1
      
#x[0] - key, x[1] - value
#x[0] 내림차순, len(x[0]) 내림차순, x[0] 오름차순으로 정렬
words = sorted(words.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))

#단어 출력
for word in words:
  print(word[0])