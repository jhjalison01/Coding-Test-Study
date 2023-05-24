from collections import deque

#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(maps):
    #answer 초기화
    INF = int(1e9)
    answer=INF
    
    n = len(maps)
    c = len(maps[0])

    
    #큐 초기화
    q=deque()
    q.append([0,0])
    
    while q:
        x,y=q.popleft()
        #상하좌우 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #maps 범위 안에 있고 값이 1일 때
            if 0<=nx and nx<n and 0<=ny and ny<c:
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    q.append([nx,ny])
    
    #상대팀 진영에 도달하지 못한 경우
    if maps[-1][-1]==1:
        answer=-1
    else: #상대팀 진영에 도달한 경우
        answer=maps[-1][-1]
    return answer