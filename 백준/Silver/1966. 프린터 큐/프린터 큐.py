import sys
from collections import deque

# 테스트 케이스의 수
case = int(sys.stdin.readline())

for i in range(case):
  n, m = map(int, input().split())
  queue = deque(list(map(int, sys.stdin.readline().split())))
  count = 0
  while queue:
    best = max(queue)  #큐의 최댓값을 저장
    front = queue.popleft() # 맨 앞에 있는 숫자를 뽑았으므로
    m -= 1 #현재 위치가 한 칸 당겨진다.

    if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
      count += 1 # 하나가 배출되므로 순번 하나 추가
      if m < 0: # m이 0이라는 것은 뽑은 숫자가 찾고자 하는 숫자라는 뜻.
        print(count)
        break

    else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
      queue.append(front) # 쿠에서 제일 뒤로 밀려나게 됨
      if m < 0 : 
        m = len(queue) - 1 # 제일 뒤로 이동