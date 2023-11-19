def solution(today, terms, privacies):
    answer = []
    dic={}
    #약관 종류에 따른 유효기간 저장
    for x in terms:
        a,b=x.split()
        dic[a]=int(b)
    #오늘 날짜 년월일로 나누어 저장
    t_year,t_month,t_day=map(int,today.split("."))
    #각 개인정보 수집 일자 확인
    for i in range(len(privacies)):
        temp,alpha=privacies[i].split()
        year,month,day=map(int,temp.split("."))
        #언제부터 파기해야하는지 구하기
        month+=dic[alpha]
        while month>12:
            month-=12
            year+=1
        
        #파기해야하는 개인정보 저장하기
        if t_year>year or (t_year==year and t_month>month) or (t_year==year and t_month==month and t_day>=day):
            answer.append(i+1)
        
    return answer