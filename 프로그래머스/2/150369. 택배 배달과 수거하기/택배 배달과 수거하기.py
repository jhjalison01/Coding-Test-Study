def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery,pickup=0,0
    
    for i in range(n):
        #멀리 있는 곳부터 배달한다.
        delivery+=deliveries[n-i-1]
        pickup+=pickups[n-i-1]
        
        while delivery>0 or pickup>0:
            delivery-=cap
            pickup-=cap
            answer+=2*(n-i) #갔다 오기 때문에 거리의 2배

    return answer