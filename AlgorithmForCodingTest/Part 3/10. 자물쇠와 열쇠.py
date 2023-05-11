#프로그래스스 2020 KAKAO BLIND RECRUITMENT
#https://school.programmers.co.kr/learn/courses/30/lessons/60059
#자물쇠의 크기를 3배로 늘려서 생각한다.

#2차원 리스트를 시계 방향으로 90도 회전
def rotate(key):
    m=len(key)
    array=[[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            array[j][m-1-i]=key[i][j]
    return array

#자물쇠 중앙 부분이 모두 1인지 확인
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)
    #자물쇠의 크기를 기존의 3배로 키운다.
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    #새로운 자물쇠 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    #4가지 방향에서 확인
    for _ in range(4):
        key=rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠 열쇠에 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                #새로운 자물쇠에 열쇠가 정확이 들어맞는지 검사
                if check(new_lock)==True:
                    return True
                #자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False
