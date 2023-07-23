def solution(phone_book):
    hash_map={}#해시 맵
    #전화번호를 해시 맵에 넣기
    for phone_number in phone_book:
        hash_map[phone_number]=1

    for phone_number in phone_book:
        temp='' #접두어
        for number in phone_number:
            temp+=number
            #접두어가 해시 맵에 있는지 확인, 해당 번호는 제외
            if temp in hash_map and temp!=phone_number:
                return False
    return True