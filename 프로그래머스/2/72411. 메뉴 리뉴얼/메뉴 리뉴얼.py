from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        cnt={} #각 코스 별 개수
        for order in orders:
            coms=list(combinations(sorted(order),c)) #조합 구하기
            #조합 별 개수 저장하기
            for com in coms:
                if com in cnt:
                    cnt[com]+=1
                else:
                    cnt[com]=1
        if cnt:
            m=max(cnt.values()) #가장 많이 함께 주문된 횟수 구하기
        if m<2:
            continue
        #최소 2명 이상 주문한 경우
        for key,value in cnt.items():
            if value==m:
                answer.append("".join(key))
    #오름차순으로 정렬
    answer.sort()
    
    return answer