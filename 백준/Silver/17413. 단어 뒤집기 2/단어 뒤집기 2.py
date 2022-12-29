import sys

strings=sys.stdin.readline().rstrip()

word=[]
tag=[]
result=""

count=0

while count!=len(strings):
    if strings[count]=='<':
        while strings[count]!='>':
            tag.append(strings[count])
            count+=1
        tag.append('>')
        count+=1
        result=result+("".join(tag))
        tag.clear()
    elif strings[count]==' ':
        result+=' '
        count+=1
    else:
        while strings[count]!=" " and strings[count]!='<':
            word.append(strings[count])
            count+=1
            if count==len(strings):
                break
        word.reverse()
        result=result+("".join(word))
        word.clear()
        
print(result)