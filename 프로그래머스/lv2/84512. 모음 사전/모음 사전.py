def solution(word):
    answer = 0
    data=['A','E','I','O','U']
    temp=''
    #길이가 1
    for i in range(5):
        if temp==word:
            break
        else:
            temp=''
        temp+=data[i]
        answer+=1
        #길이가 2
        for j in range(5):
            if temp==word:
                break
            else:
                temp=temp[:1]
            temp+=data[j]
            answer+=1
            #길이가 3
            for k in range(5):
                if temp==word:
                    break
                else:
                    temp=temp[:2]
                temp+=data[k]
                answer+=1
                #길이가 4
                for x in range(5):
                    if temp==word:
                        break
                    else:
                        temp=temp[:3]
                    temp+=data[x]
                    answer+=1
                    #길이가 5
                    for y in range(5):
                        if temp==word:
                            break
                        else:
                            temp=temp[:4]
                        temp+=data[y]
                        answer+=1
    return answer
