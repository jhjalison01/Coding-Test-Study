from collections import deque

def check(deck1,deck2,target):
    for card in deck1:
        #2장의 카드 제출
        if target-card in deck2:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False #카드 제출 못함

def solution(coin, cards):
    
    n=len(cards)
    #손에 있는 카드
    hand=cards[:n//3]
    #뽑을 카드
    deck=deque(cards[n//3:])
    #뽑은 카드
    draw = []
    answer=1
    
    while coin >= 0 and deck:
        #deck에서 2장 뽑기
        draw.append(deck.popleft())
        draw.append(deck.popleft())
        
        #코인을 안 써도 되는 경우:
        if check(hand, hand, n+1):
            pass
        #코인을 한 개 쓸 경우
        elif coin>=1 and check(hand, draw,n+1):
            coin-=1
        #코인을 두 개 쓸 경우
        elif coin>=2 and check(draw, draw,n+1):
            coin-=2
        else:
            break
        answer+=1
    
    return answer