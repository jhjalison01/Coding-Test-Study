import sys

bar_razor=sys.stdin.readline().rstrip()
bar_razor=list(bar_razor.replace("()",'r'))

stack=[]
result=0

for i in bar_razor:
    if i=='(':
        stack.append('(')
    elif i=='r':
        result+=len(stack)
    elif i==')':
        stack.pop()
        result+=1

print(result)