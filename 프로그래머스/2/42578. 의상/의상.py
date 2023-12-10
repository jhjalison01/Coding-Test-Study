def solution(clothes):
    answer = 1
    dic={}
    
    #딕셔너리에 삽입
    for c in clothes:
        if c[1] in dic:
            dic[c[1]].append(c[0])
        else:
            dic[c[1]]=[c[0]]
            
    #경우의 수 구하기
    for val in dic.values():
        n=len(val)+1
        answer*=n
    return answer-1