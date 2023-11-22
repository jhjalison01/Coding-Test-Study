def solution(id_list, report, k):
    answer = []
    id_dic={} #신고 받은 id: (신고한 사람들 id)
    for i in id_list:
        id_dic[i]=set()
    #신고한 사람들 id 저장
    for re in report:
        giver,receiver=re.split()
        id_dic[receiver].add(giver)
    
    result={} # id: 받을 처리 결과 메일 개수
    for i in id_list:
        result[i]=0
    #신고한 사람이 k 이상일 경우 받을 처리 결과 메일 개수 증가
    for key,value in id_dic.items():
        if len(value)>=k:
            for i in value:
                result[i]+=1
    #value를 리스트로 옮기기            
    for key, val in result.items():
        answer.append(val)
    
    return answer