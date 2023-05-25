from collections import deque

def solution(n, computers):
    answer = 0
    visited=[False]*n
    
    def bfs(start, visited, computers):
        visited[start]=True
        q=deque()
        q.append(start)
        while q:
            v=q.popleft()
            for i in range(n):
                if computers[v][i]==1 and not visited[i]:
                    q.append(i)
                    visited[i]=True
                    
    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers)
            answer+=1
        
    return answer