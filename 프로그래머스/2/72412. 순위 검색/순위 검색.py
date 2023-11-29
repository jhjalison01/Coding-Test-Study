from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic=defaultdict(list)
    #한 명의 지원자씩 확인
    for info in information:
        info=info.split()
        score=int(info[-1])
        condition=info[:-1]
        #한 명의 지원자는 16가지 그룹에 속하게 된다.
        for i in range(5):
            # "-"가 어느 위치에 들어갈지 구하기
            case=list(combinations([0,1,2,3],i))
            for c in case:
                temp=condition.copy()
                for idx in c:
                    temp[idx]="-"
                key="".join(temp)
                #해당되는 그룹에 점수 저장
                dic[key].append(score)
    
    #이분 탐색을 위해 각 그룹의 점수를 오름차순으로 정렬
    for value in dic.values():
        value.sort()
    
    #query 각각 확인
    for query in queries:
        query=query.replace("and ","")
        query=query.split()
        target_key="".join(query[:-1])
        target_score=int(query[-1])
        result=0
        if target_key in dic:
            target_list=dic[target_key]
            #bisect_left: lower bound, 원하는 값 이상이 처음 나오는 위치를 찾음
            idx=bisect_left(target_list,target_score)
            result=len(target_list)-idx
        answer.append(result)
    
    
    return answer