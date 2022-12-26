import sys

N, K=map(int,sys.stdin.readline().split())
circle=[]
point=0
result=[]

for i in range(N):
    circle.append(i+1)

for i in range(N):
    point=(point+K-1)%len(circle)
    result.append(str(circle.pop(point)))



print("<%s>" %(", ".join(result)))