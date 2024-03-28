import sys
input=sys.stdin.readline

quack = 'quack'
sound=input().rstrip()
visited = [False] * len(sound)
cnt=0 #오리의 수

def find(start):
  global cnt
  point=0 #quack 위치
  is_first=True
  for i in range(start, len(sound)):
    if sound[i] == quack[point] and not visited[i]:
      visited[i]=True
      if sound[i] == 'k':
        if is_first:
          is_first=False
          cnt+=1 #한 마리의 오리가 계속 울 수도 있기 때문에 한 번만 카운트
        point=0 #quack 위치 다시 처음으로
      else: #k가 아닐 경우 다음 문자 탐색
        point+=1

if len(sound)%5!=0: #입력된소리의 길이가 5의 배수가 아닐 경우 올바른 울음소리가 아님
  print(-1)
  exit() #실행 종료

for i in range(len(sound)):
  #탐색하지 않은 q일 경우
  if sound[i] =='q' and not visited[i]:
    find(i)

#오리가 0마리 이거나 모든 문자를 방문하지 않았을 경우
if cnt==0 or not all(visited):
  print(-1)
else: #올바른 울음소리일 경우
  print(cnt)