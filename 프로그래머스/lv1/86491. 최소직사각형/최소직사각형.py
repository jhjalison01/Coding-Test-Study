def solution(sizes):
    answer = 0
    w=[]
    h=[]
    
    #가로, 세로 길이 중 긴 것을 w에 넣고 짧은 것을 h에 넣기
    for x in sizes:
        if x[0]>=x[1]:
            w.append(x[0])
            h.append(x[1])
        else:
            w.append(x[1])
            h.append(x[0])
            
    #두 개의 리스트에서 가장 큰 값끼리 곲하기
    answer=max(w)*max(h)
     
    return answer