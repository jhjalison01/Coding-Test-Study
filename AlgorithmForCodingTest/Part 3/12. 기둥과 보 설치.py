#이것이 취업을 위한 코딩 테스트다 Part3 구현 12. 기둥과 보 설치

#기둥 - 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#보 - 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

#build_frame [x,y,a,b]
# x,y 좌표
#a 0 - 기둥, 1 - 보
#b 0 - 삭제, 1 - 설치

#answer [x,y,a]
#a 0 - 기둥, 1 - 보
#x 좌표 기준 오른차순 정렬

def possible(answer):
  for ans in answer:
    x,y,a=ans
    if a==0: #설치된 것이 기둥일 때
      #바닥 위, 다른 기둥 위, 보의 한쪽 끝 부분 위
      if y==0 or [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
        continue
      return False
    elif a==1: #설치된 것이 보일 때
      #한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보 위
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
        continue
      return False
  return True

def solution(n, build_frame):
  answer = []

  for frame in build_frame:
    x,y,a,b=frame
    if b==0: #삭제할 때
      answer.remove([x,y,a]) # 일단 삭제한다
      if not possible(answer):
        answer.append([x,y,a]) #삭제 불가능하면 다시 설치
    elif b==1: #설치할 때
      answer.append([x,y,a]) #일단 설치한다
      if not possible(answer):
        answer.remove([x,y,a])
  return sorted(answer) #설치 불가능하면 다시 삭제
