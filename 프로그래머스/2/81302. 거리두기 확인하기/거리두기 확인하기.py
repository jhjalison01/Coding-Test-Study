from collections import deque

def bfs(place):
    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    #P가 있는 위치 저장
    start=[]
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                start.append([i,j])

    for s in start:
        queue=deque([s])
        visited=[[0]*5 for _ in range(5)]
        distance=[[0]*5 for _ in range(5)]
        visited[s[0]][s[1]]=1

        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                #범위 내에 있고 아직 확인하지 않는 곳일 경우
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0:
                    #빈 테이블일 경우
                    if place[nx][ny]=='O':
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                        distance[nx][ny]=distance[x][y]+1
                    #응시자일 경우 이전 지점의 distance 값이 1이하일 경우
                    if place[nx][ny]=='P' and distance[x][y]<=1:
                        return 0 #거리두기를 하지 않았으므로 0을 리턴
    return 1 #모든 응시자가 거리두기를 지켰으면 1을 리턴

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))

    return answer