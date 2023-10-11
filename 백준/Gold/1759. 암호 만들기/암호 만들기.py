import sys
input=sys.stdin.readline

#암호 길이, 알파벳 개수
L,C=map(int,input().split())
#알파벳 입력 받기
data=input().split()
data.sort() #암호는 알파벳이 증가하는 순서로 배열되므로 오름차순으로 정렬
#모음
vowels=['a','e','i','o','u']

def sol(pw,idx):
  #암호 길이가 L일 경우
  if len(pw)==L:
    vowel=0
    consonant=0
    #모음, 자음 개수 구하기
    for i in pw:
      if i in vowels:
        vowel+=1
      else:
        consonant+=1
    #최소 한 개의 모음, 최소 두 개의 자음으로 구성됐을 경우
    if vowel>=1 and consonant>=2:
      print(pw) #해당 암호 출력
    return
  #암호 만들기
  for i in range(idx,C):
    pw+=data[i] #암호에 알파벳 추가
    sol(pw,i+1) #백트래킹 실행
    pw=pw[:-1] #암호에 알파벳 제거

sol("",0)