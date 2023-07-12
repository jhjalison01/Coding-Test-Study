n=int(input())
data=[]

for i in range(n):
  data.append(int(input()))

data.sort(reverse=True)
answer=data[0]

for i in range(n):
  if data[i]*(i+1)>=answer:
    answer=data[i]*(i+1)

print(answer)