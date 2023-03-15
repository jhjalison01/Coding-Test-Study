import sys
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'

while True:
  data=sys.stdin.readline().rstrip('\n')
  if not data:
    break

  count=[0]*4
  for i in range(len(data)):
    if data[i] in lower:
      count[0]+=1
    elif data[i] in upper:
      count[1]+=1
    elif data[i]==' ':
      count[3]+=1
    else:
      count[2]+=1
  print(*count)