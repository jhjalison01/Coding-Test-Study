import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
  right=[]
  left=[]
  word=input().strip()
  for w in word:
    if w=="-": #왼쪽 스택 요소 삭제
      if left:
        left.pop()
    elif w=="<": #왼쪽 스택 요소를 오른쪽 스택으로 옮기기
      if left:
        right.append(left.pop())
    elif w==">": #오른쪽 스택 요소를 왼쪽 스택으로 옮기기
      if right:
        left.append(right.pop())
    else: #왼쪽 스택에 넣기
      left.append(w)
  left.extend(reversed(right))
  print("".join(left))