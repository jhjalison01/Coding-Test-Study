import sys
input=sys.stdin.readline

#01 - 1번
#010 - 1번
#0101 - 2번
#01010 - 2번
#010101 - 3번
s=input().rstrip()
cnt=0

for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    cnt+=1
print((cnt+1)//2)