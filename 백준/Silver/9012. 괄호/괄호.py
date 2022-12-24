import sys

n=int(sys.stdin.readline())

for i in range(n):
    words=sys.stdin.readline().rstrip()
    while words.find("()")!=-1:
        a=words.find("()")
        words=list(words)
        words.pop(a+1)
        words.pop(a)
        words="".join(words)
    if len(words)==0:
        print("YES")
    else:
        
        print("NO")