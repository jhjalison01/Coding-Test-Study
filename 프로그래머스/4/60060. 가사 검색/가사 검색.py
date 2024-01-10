from bisect import bisect_left, bisect_right

def count_by_range(arr,left_value,right_value):
    right_index=bisect_right(arr,right_value)
    left_index=bisect_left(arr, left_value)
    return right_index-left_index

def solution(words, queries):
    answer = []
    
    array=[[] for _ in range(10001)]
    reversed_array=[[] for _ in range(10001)]
    
    #길이가 같은 것끼리 같은 배열에 넣기
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입
    
    #이분 탐색을 위해 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0]=='?': #접두사에 ?가 붙은 경우
            result=count_by_range(reversed_array[len(q)],q[::-1].replace("?","a"),q[::-1].replace("?","z"))
        else: #접미사에 ?가 붙은 경우
            result=count_by_range(array[len(q)],q.replace("?","a"),q.replace("?","z"))
        answer.append(result)
        
    return answer