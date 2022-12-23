import sys

n=int(sys.stdin.readline())
for i in range(n):
    sentence=sys.stdin.readline()
    li=sentence.split()
    for j in range(len(li)):
        li[j]="".join(reversed(li[j]))
    print(" ".join(li))