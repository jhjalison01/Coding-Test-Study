while True:
  try:
    a=input().rstrip()
    b=input().rstrip()
    #set으로 바꾸기
    a_set=set(a)
    b_set=set(b)
    x=a_set & b_set #교집합 구하기
    answer=[]
    for w in x:
      #각 문자열에 w가 몇 번 등장하는지 카운트
      answer.append(w * min(a.count(w),b.count(w)))
    answer.sort()
    print("".join(answer))
  except:
    break