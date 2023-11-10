def solution(survey, choices):
    answer = ''
    #첫번째-비동의
    #두번째-동의
    check={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0} #각 항목당 점수
    types=["RT","CF","JM","AN"]
    #검사 실행
    for i in range(len(survey)):
        if choices[i]==1:
            check[survey[i][0]]+=3
        elif choices[i]==2:
            check[survey[i][0]]+=2
        elif choices[i]==3:
            check[survey[i][0]]+=1
        elif choices[i]==5:
            check[survey[i][1]]+=1
        elif choices[i]==6:
            check[survey[i][1]]+=2
        elif choices[i]==7:
            check[survey[i][1]]+=3
            
    #검사 결과 확인
    for i in range(4):
        #2번째 지표가 더 클 경우
        if check[types[i][0]]<check[types[i][1]]:
            answer+=types[i][1]
        else: #1번째 지표가 더 크거나 두 지표의 값이 같을 경우
            answer+=types[i][0]
    
    return answer