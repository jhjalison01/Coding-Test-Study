#이것이 취업을 위한 코딩 테스트다 Part3 DFS/BFS 18. 괄호 변환

#균형잡힌 괄호 문자열 - '(' 의 개수와 ')' 의 개수가 같은 경우
#올바른 괄호 문자 - '('와 ')'의 괄호의 짝도 모두 맞을 경우

#균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
  count=0
  for i in range(len(p)):
    if p[i]=='(':
      count+=1
    else:
      count-=1
    if count==0: # '('와 ')'의 개수가 같을 때
      return i

#올바른 괄호 문자열인지 확인
def check_proper(p):
  count=0
  for i in p:
    if i=='(':
      count+=1
    else:
      if count==0: #쌍이 맞지 않는 경우 False 반환
        return False
      count-=1
  return True #쌍이 맞는 경우 True 반

def solution(p):
  answer=''
  if p=='': # 빈 문자열인 경우 빈 문자열 반환
    return ''
  # u,v 분리
  index=balanced_index(p)
  u=p[:index+1]
  v=p[index+1:]
  #u가 올바른 괄호 문자열일 경우
  if check_proper(u):
    answer=u+solution(v)
  #u가 올바른 괄호 문자열이 아닐 경우
  else:
    answer='('
    answer+=solution(v)
    answer+=')'
    #u의 첫번째, 마지막 문자 제거
    u=list(u[1:-1])
    #u의 나머지 괄호 방향 뒤집기
    for i in range(len(u)):
      if u[i]=='(':
        u[i]=')'
      else:
        u[i]='('
    answer+="".join(u)
  return answer
