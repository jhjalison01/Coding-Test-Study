import sys
from collections import Counter

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
operator=['+','-','*','/']
stack=[]
nums=[]

n=int(sys.stdin.readline().rstrip())
calculate=list(sys.stdin.readline().rstrip())

for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

for i in calculate:
    if i in operator:
        a=stack.pop()
        b=stack.pop()
        if i =='+':
            stack.append(a+b)
        elif i=='-':
            stack.append(b-a)
        elif i=='*':
            stack.append(a*b)
        elif i=='/':
            stack.append(b/a)
    else:
        stack.append(nums[alphabet.find(i)])

print('%.2f' %stack[0])