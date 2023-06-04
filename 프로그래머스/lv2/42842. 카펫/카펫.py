def solution(brown, yellow):
    answer = []
    #노란색 격자의 약수를 각각 가로, 세로 길이로 가정
    for i in range(1,yellow+1):
        if yellow%i==0:
            h=i
            w=yellow//i
            #가정한 노란색 격자를 감싸는 갈색 격자 수와 주어진 격자 수가 같을 경우
            if (w+h)*2+4==brown:
                #노란색 격자의 가로, 세로 길이에 각각 2씩 더하여 카펫의 길이를 구하기
                answer.append(w+2)
                answer.append(h+2)
                break
    return answer