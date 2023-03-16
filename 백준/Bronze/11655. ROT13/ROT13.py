data=input()
result=''

for a in data:
  if a.isupper():
    num=ord(a)
    if (num+13)>90:
      num-=13
    else:
      num+=13
    result+=chr(num)
  elif a.islower():
    num=ord(a)
    if (num+13)>122:
      num-=13
    else:
      num+=13
    result+=chr(num)
  else:
    result+=a

print(result)