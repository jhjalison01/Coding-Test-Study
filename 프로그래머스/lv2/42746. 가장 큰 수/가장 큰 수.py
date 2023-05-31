def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) #정수를 문자열로 바꾸기
    # 문자열을 3번 뒤에 더하여 비교하는 이유 : 비교 하는 숫자들의 자리수를 맞춰서 비교를 해보기 위해, number는 1000이하의 숫자로 이루어져있기 때문
    # [3, 30, 34, 5, 9] -> [999, 555, 343434, 303030, 333]
    numbers.sort(key=lambda x : x*3,reverse=True)
    #int로 먼저 바꾸는 이유 : numbers가 [0,0,0,0]일 경우 0으로 나타내기 위해
    answer=str(int(''.join(numbers)))
    
    return answer