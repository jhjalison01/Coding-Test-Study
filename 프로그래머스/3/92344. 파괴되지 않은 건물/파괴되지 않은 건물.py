def solution(board, skills):
    answer = 0 #파괴되지 않은 건물의 개수

    n=len(board)
    m=len(board[0])
    tmp=[[0]*(m+1) for _ in range(n+1)] #누적합 기록을 위한 배열
    
    #누적합 구하기
    for ty,x1,y1,x2,y2,degree in skills:
        #공격일 경우
        if ty==1:
            degree=-degree
            
        tmp[x1][y1]+=degree
        tmp[x2+1][y2+1]+=degree
        tmp[x1][y2+1]-=degree
        tmp[x2+1][y1]-=degree
    
    #위에서 아래로 누적합
    for i in range(n):
        for j in range(m):
            tmp[i+1][j]+=tmp[i][j]
    #왼쪽에서 오른쪽으로 누적합
    for i in range(n):
        for j in range(m):
            tmp[i][j+1]+=tmp[i][j]
    
    #누적합을 기존 배열에 더하기
    for i in range(n):
        for j in range(m):
            board[i][j]+=tmp[i][j]
            #내구도 1이상인 경우
            if board[i][j]>=1:
                answer+=1
    
    return answer