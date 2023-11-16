def solution(record):
    answer = []
    result={} #유저 아이디에 대한 닉네임 저장

    for word in record:
        temp=word.split()
        if len(temp)==3: #Enter, Change일 경우
            first,user_id,nickname=temp[0],temp[1],temp[2]
            result[user_id]=nickname #닉네임 정보 저장 or 업데이트
            
    for word in record:
        temp=word.split()
        first,user_id=temp[0],temp[1]
        if first=="Enter":
            answer.append(result[user_id]+"님이 들어왔습니다.")
        elif first=="Leave":
            answer.append(result[user_id]+"님이 나갔습니다.")
    return answer