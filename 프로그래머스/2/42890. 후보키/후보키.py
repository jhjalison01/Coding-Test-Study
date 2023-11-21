from itertools import combinations

def check(num,result):
    for x in range(1,len(num)+1):
        for y in list(combinations(num,x)):
            if y in result:
                return False
    return True

def solution(relation):
    answer = 0
    
    n=len(relation[0])
    row=len(relation)
    nums=[0,1,2,3,4,5,6,7]
    nums=nums[:n]
    result=[]
    
    for i in range(1,n+1):
        for num in list(combinations(nums,i)):
            temp=[]
            a=""
            flag=True
            #유일성 확인
            for r in range(row):
                #속성끼리 합치기
                for index in num:
                    a+=relation[r][index]
                #유일성에 어긋날 경우
                if a in temp:
                    flag=False
                    break
                temp.append(a)
                a=""
            #유일성 갖고 있을 경우
            if flag:
                #최소성 확인
                if check(num,result):
                    result.append(num)
    
    answer=len(result)
    return answer