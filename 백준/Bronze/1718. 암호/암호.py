import sys
input=sys.stdin.readline

word=input().rstrip()
key=input().rstrip()

result=""
for i in range(len(word)):
  if word[i]==" ":
    result+=" "
  else:
    #암호화하려는 문장 (평문)의 단어와 암호화 키를 숫자로 바꾼 다음, 평문의 단어에 해당하는 숫자에 암호 키에 해당하는 숫자를 더함
    result+=chr(ord("a")+(ord(word[i])-ord(key[i%len(key)])-1)%26)

print(result)