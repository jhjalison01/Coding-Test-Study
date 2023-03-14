s = input()
  
data='abcdefghijklmnopqrstuvwxyz'
count=[]

for i in range(len(data)):
  count.append(s.count(data[i]))

for j in count:
  print(j,end=" ")