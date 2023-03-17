s=input()
li=[]

for i in range(len(s)):
  li.append(s[i:])

li.sort()
print(*li,sep="\n")