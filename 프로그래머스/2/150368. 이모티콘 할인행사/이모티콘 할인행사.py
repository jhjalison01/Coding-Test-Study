from itertools import product

def solution(users, emoticons):
    answer = []
    n_emo=len(emoticons)
    #할인율은 10%, 20%, 30%, 40% 중 하나이므로 모든 경우를 확인
    for discounts in list(product([10,20,30,40], repeat = n_emo)):
        result=[0,0] #result[0]: 이모티콘 플러스 가입자 수, result[1]: 판매액
        #한 사람당 이모티콘을 얼마나 사는지 확인
        for user in users:
            total=0 #한 사람의 이모티콘 구매 비용
            for i in range(n_emo):
                #사용자가 이모티콘을 구매할 경우
                if discounts[i]>=user[0]:
                    total+=emoticons[i]*(1-discounts[i]*0.01)
            #이모티콘 플러스를 가입할 경우
            if total>=user[1]:
                result[0]+=1
            else:
                result[1]+=total
        answer.append(result)
    #이모티콘 플러스 가입자가 많고 판매액이 많은 순으로 정렬
    answer.sort(key=lambda x:(-x[0],-x[1]))
    
    return answer[0]