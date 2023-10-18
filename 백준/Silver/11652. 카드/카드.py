import sys
input=sys.stdin.readline
#준규가 갖고 있는 카드 개수
n=int(input())
dic={} #딕셔너리

for i in range(n):
  a=int(input())
  if a in dic.keys():
    dic[a]+=1
  else:
    dic[a]=1
    
#카드 개수를 내림차순으로, 카드 숫자를 오름차순으로 정렬
dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))

print(dic[0][0])