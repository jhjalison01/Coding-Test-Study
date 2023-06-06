count=0

def dfs(v,graph,visited):
    global count
    visited[v]=True
    count+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i,graph,visited)
    return count

def solution(n, wires):
    global count
    answer = n
    graph=[[] for i in range(n+1)]
    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    for i in range(len(wires)):
        temp=graph.copy()
        temp[wires[i][0]].remove(wires[i][1])
        temp[wires[i][1]].remove(wires[i][0])
        visited=[False]*(n+1)
        count=0
        a=dfs(wires[i][0],temp,visited)
        count=0
        b=dfs(wires[i][1],temp,visited)
        print(a,b)
        answer=min(answer,abs(a-b))
        temp[wires[i][0]].append(wires[i][1])
        temp[wires[i][1]].append(wires[i][0])
        
    return answer
