from collections import deque

def solution(board):
    def bfs(start):
        INF=int(1e9)
        #상하좌우
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
    
        n=len(board)
        visited=[[INF]*n for _ in range(n)]
        visited[0][0]=0

        q=deque([start])
        while q:
            x,y,cost,d=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                    #직진일 경우
                    if i==d:
                        ncost=cost+100
                    #꺾을 경우
                    else:
                        ncost=cost+600
                    #최소 비용 갱신
                    if ncost<visited[nx][ny]:
                        visited[nx][ny]=ncost
                        q.append([nx,ny,ncost,i])
        #도착했을 때 든 비용 리턴
        return visited[-1][-1] 
    
    #아래로 갈 경우, 오른쪽으로 갈 경우
    return min([bfs((0,0,0,1)),bfs((0,0,0,3))])