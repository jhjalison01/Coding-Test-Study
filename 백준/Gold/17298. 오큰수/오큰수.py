import sys

n=int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
stack=[]
answer=[-1 for i in range(n)]

for i in range(n):
    while stack and arr[stack[-1]]<arr[i]:
        answer[stack.pop()]=arr[i]
    stack.append(i)
print(*answer)
