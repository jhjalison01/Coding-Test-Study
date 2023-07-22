def solution(participant, completion):
    hashDict={}
    sumHash=0
    #participant의 총 해시 값 구하기
    for p in participant:
        hashDict[hash(p)]=p
        sumHash+=hash(p)
    #completion의 총 해시 값 구하기
    for c in completion:
        sumHash-=hash(c)
    #남은 값이 완주하지 못한 선수의 해시 값이 됨
    return hashDict[sumHash]
    