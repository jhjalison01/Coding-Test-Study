from collections import defaultdict

def solution(friends, gifts):
    answer = 0 #다음 달 선물을 가장 많이 받을 친구가 받을 선물의 수
    
    gifted = dict() #주고 받은 선물 기록할 딕셔너리
    gift_idx = dict() #선물 지수 기록할 딕셔너리
    
    #주고 받은 선물, 선물 지수 딕셔너리 초기화
    for friend in friends:
        gifted[friend]=dict()
        gift_idx[friend]=0
        
    #주고 받은 선물 기록, 선물 지수 기록
    for gift in gifts:
        #giver: 선물 준 사람, receiver: 선물 받은 사람
        giver,receiver = gift.split()
        
        if receiver in gifted[giver]:
            gifted[giver][receiver]+=1
        else:
            gifted[giver][receiver]=1
        
        gift_idx[giver]+=1
        gift_idx[receiver]-=1
        
    #다음 달 받을 선물 카운트 할 딕셔너리
    cnt=defaultdict(int)
    #다음 달 받을 선물 카운트
    for i in range(len(friends)):
        curr=friends[i] #현재 사람
        for j in range(i+1,len(friends)):
            another=friends[j] #다른 사람
            #curr가 another에 준 선물 개수
            curr_cnt=gifted[curr][another] if another in gifted[curr] else 0
            #another가 curr에게 준 선물 개수
            another_cnt=gifted[another][curr] if curr in gifted[another] else 0
            
            #더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음
            if curr_cnt>another_cnt:
                cnt[curr]+=1
            elif another_cnt>curr_cnt:
                cnt[another]+=1
            #주고받은 선물 수가 같을 경우
            #선물 지수(준 선물의 수-받은 선물의 수)가 더 큰 사람이 작은 사람에게 선물을 하나 받음
            elif curr_cnt==another_cnt:
                if gift_idx[curr]>gift_idx[another]:
                    cnt[curr]+=1
                elif gift_idx[another]>gift_idx[curr]:
                    cnt[another]+=1
            
    if cnt:
        answer=max(list(cnt.values()))
    
    return answer