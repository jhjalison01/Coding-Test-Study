import sys
input=sys.stdin.readline

r,c,k=map(int,input().split())

arr=[]
for _ in range(3):
  arr.append(list(map(int,input().split())))

def sol(arr, RC):
  sorted_arr=[]
  max_cnt=0
  for i in range(len(arr)):
    tmp=[]
    #숫자 개수 카운트
    dict={}
    for j in range(len(arr[i])):
      if arr[i][j]!=0:
        if arr[i][j] not in dict:
          dict[arr[i][j]]=1
        else:
          dict[arr[i][j]]+=1
    #[숫자,숫자 개수] 저장, 정렬
    for key,value in dict.items():
      tmp.append([key,value])
    tmp.sort(key=lambda x:[x[1],x[0]])
    #1차원 배열로 바꾸기
    tmp_flatten=sum(tmp,[])
    max_cnt=max(max_cnt,len(tmp_flatten))
    sorted_arr.append(tmp_flatten)
    
  for i in sorted_arr:
    #가장 긴 길이에 맞춰서 0 추가
    i+=[0]*(max_cnt-len(i))
    #길이가 100이 넘을 경우 처음 100개를 제외한 나머지 버리기
    if len(i)>100:
      i=i[:100]
  #C 연산일 경우 행,열 바꾸기
  return sorted_arr if RC=="R" else list(zip(*sorted_arr))

cnt=0 #시간

while cnt<101:
  if r-1<len(arr) and c-1<len(arr[0]):
    if arr[r-1][c-1]==k:
      break
  if len(arr)>=len(arr[0]):
    #R 연산
    arr=sol(arr,"R")
  else:
    #C 연산
    arr=sol(list(zip(*arr)),"C")
  cnt+=1
    

if cnt==101:
  print(-1)
else:
  print(cnt)