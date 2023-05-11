def solution(s):
    answer = len(s)

    #1개의 단위부터 압축 단위를 늘려가며 확인
    for i in range(1,len(s)//2+1):
        now_string=""
        previous=s[:i] #앞에서부터 i만큼 추출
        count=1
        #단위(i) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(i,len(s),i):
            now=s[j:j+i]
            #이전 문자열과 동일하면 count 증가
            if now==previous:
                count+=1
            #이전 문자열과 다를 경우
            else:
                if count>1:
                    now_string+=str(count)+previous
                else:
                    now_string+=previous
                count=1
                previous=now

        #나머지 문자열 처리
        if count>1:
            now_string+=str(count)+previous
        else:
            now_string+=previous
        
        #압축된 문자열 중 가장 짧은 것을 정답으로 대입
        answer=min(answer,len(now_string))
    
    return answer
