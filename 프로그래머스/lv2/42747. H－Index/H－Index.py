def solution(citations):
    #내림차순으로 정렬
    citations.sort(reverse=True)
    #h편의 논문이 h회 이상 인용된 경우 찾기
    for idx , citation in enumerate(citations):
        if citation<=idx:
            return idx
    return len(citations)