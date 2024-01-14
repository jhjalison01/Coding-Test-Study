def solution(alp, cop, problems):
    INF=int(1e9) #무한대 값
    #목표 알고력, 목표 코딩력 구하기
    alp_max,cop_max=0,0
    for problem in problems:
        alp_max=max(alp_max,problem[0])
        cop_max=max(cop_max,problem[1])
    #목표 알고력, 목표 코딩력을 넘으면 안 됨
    alp=min(alp,alp_max)
    cop=min(cop,cop_max)
    #dp[i][j] - 알고력 i, 코딩력 j에 도달하는데 걸리는 최단 시간
    dp=[[INF for _ in range(cop_max+1)] for _ in range(alp_max+1)]
    dp[alp][cop]=0
    
    for i in range(alp,alp_max+1):
        for j in range(cop,cop_max+1):
            #알고력 1 증가시키기
            if i+1<=alp_max:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)
            #코딩력 1 증가시키기
            if j+1<=cop_max:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)
            #문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>=alp_req and j>=cop_req:
                    new_alp=min(i+alp_rwd,alp_max)
                    new_cop=min(j+cop_rwd,cop_max)
                    dp[new_alp][new_cop]=min(dp[new_alp][new_cop],dp[i][j]+cost)
    return dp[alp_max][cop_max]