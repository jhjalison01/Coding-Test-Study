import sys
input=sys.stdin.readline

from math import ceil

#주차 요금 계산
def sol(fees, time):
    result=fees[1]
    if time>fees[0]:
        print("time:",time,"fees[0]:",fees[0])
        print((time-fees[0]))
        result+=ceil((time-fees[0])/fees[2])*fees[3]
    return result

def solution(fees, records):
    answer = []
    in_time={}
    total_time={}
    for record in records:
        time, number, in_out=record.split()
        #입차일 경우
        if in_out=="IN":
            in_time[number]=time
        else: #출차일 경우
            hour,minute=map(int,time.split(":"))
            in_hour, in_minute=map(int,in_time[number].split(":"))
            #주차 시간 계산
            if number not in total_time:
                total_time[number]=(hour*60+minute)-(in_hour*60+in_minute)
            else:
                total_time[number]+=(hour*60+minute)-(in_hour*60+in_minute)
            in_time[number]=0

    #in이 되어있지만 out이 되어있지 않은 차량
    for num in in_time:
        if in_time[num]!=0:
            in_hour, in_minute=map(int,in_time[num].split(":"))
            #11:50분에 출차된 것으로 간주
            if num not in total_time:
                total_time[num]=(23*60+59)-(in_hour*60+in_minute)
            else:
                total_time[num]+=(23*60+59)-(in_hour*60+in_minute)
                          
    for num,time in sorted(total_time.items(),key=lambda x:x[0]):
        answer.append(sol(fees,time))

    return answer