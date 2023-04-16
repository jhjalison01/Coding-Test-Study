import sys

n=int(sys.stdin.readline().rstrip())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().rstrip())
m_list=list(map(int,sys.stdin.readline().split()))

result=[]
n_list.sort()

def binary_search(array,target,start,end):
  if start>end:
    return False
  mid=(start+end)//2
  if target==array[mid]:
    return True
  elif target>array[mid]:
    return binary_search(array,target,mid+1,end)
  else:
    return binary_search(array,target,start,mid-1)

for i in m_list:
  if binary_search(n_list,i,0,n-1):
    print(1)
  else:
    print(0)