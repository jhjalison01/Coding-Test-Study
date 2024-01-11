import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

answer = 'z'
def solution(n, m, x1, y1, x2, y2, k):
    result=[]
    dx=[1, 0, 0, -1]
    dy=[0, -1, 1, 0]
    paths=['d', 'l', 'r', 'u']
    
    def dfs(x,y,path):
        global answer
        #도착할 수 없을 경우
        if k < len(path)+abs(x - x2) + abs(y - y2):
            return
        #조건에 맞게 도착할 경우
        if len(path)==k and x==x2 and y==y2:
            answer=path
            return
        #아래, 왼쪽, 오른쪽, 위쪽 순으로 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 1<=nx<=n and 1<=ny<=m and path<answer:
                dfs(nx,ny,path+paths[i])
        
    #최소 거리 구하기
    dis=abs(x1-x2)+abs(y1-y2)
    #도착할 수 없을 경우
    if dis>k or dis%2!=k%2 :
        return "impossible"
    dfs(x1,y1,"")
    
    return answer