import sys

n=int(sys.stdin.readline())
sequence=[]
stack=[]
result=[]
count=0
push_pop=[]

for i in range(n):
    sequence.append(int(sys.stdin.readline()))


for j in range(1,n+1):
    stack.append(j)
    push_pop.append('+')

    while stack[-1]==sequence[count]:
        result.append(stack.pop())
        count+=1
        push_pop.append('-')
        if len(stack)==0:
            break
        
if result==sequence:
    for i in push_pop:
        print(i)
else:
    print("NO")