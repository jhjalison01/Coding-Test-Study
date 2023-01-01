import sys
from collections import Counter

n=int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr_count=Counter(arr)
stack=[]
answer=[-1 for i in range(n)]

for i in range(n):
    while stack and arr_count[arr[stack[-1]]]<arr_count[arr[i]]:
        answer[stack.pop()]=arr[i]
    stack.append(i)
print(*answer)