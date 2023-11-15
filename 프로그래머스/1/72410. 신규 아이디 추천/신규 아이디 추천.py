def solution(new_id):
    data=["-","_","."]
    #1단계
    result=new_id.lower()
    #2단계
    temp=""
    for x in result:
        if x.isalpha() or x.isdigit() or x in data:
            temp+=x
    result=temp
    #3단계
    while ".." in result:
        result=result.replace("..",".")
    #4단계
    if result:
        if result[0]==".": result=result[1:]
        if result:
            if result[-1]==".": result=result[:-1]
    #5단계
    if not result:
        result+="a"
    #6단계
    if len(result)>=16:
        result=result[:15]
        if result[-1]==".":
            result=result[:-1]
    #7단계
    if len(result)<=2:
        while len(result)<3:
            result+=result[-1]
    
    return result