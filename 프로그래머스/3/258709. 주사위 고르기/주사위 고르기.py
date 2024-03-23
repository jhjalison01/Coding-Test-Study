from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    #key: 이길 수 있는 경우의 수, value: 주사위 번호들
    dic = {}
    L = len(dices)
    #주사위 나누기
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]
        #만들 수 있는 주사위의 합 구하기
        A_sum, B_sum = [],[]
        for order_product in product(range(6),repeat=L//2):
            A_sum.append(sum(dices[i][j] for i,j in zip(A_index_combi, order_product)))
            B_sum.append(sum(dices[i][j] for i,j in zip(B_index_combi, order_product)))
        B_sum.sort()
        
        #이진 탐색
        #wins: A가 B를 이길 수 있는 경우의 수
        wins = sum(bisect_left(B_sum, num) for num in A_sum)
        dic[wins]=list(A_index_combi)
    #A가 이길 수 있는 경우의 수 중 최댓값
    max_key=max(dic.keys())
    
    return [x+1 for x in dic[max_key]]