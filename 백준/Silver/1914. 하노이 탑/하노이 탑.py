n=int(input())

#start-처음 원판이 있는 장대, end-최종 장대, tmp-임시 장대
def hanoi(n,start,end,tmp):
  if n==1:
    print(start,end)
    return
  #n-1개의 원판을 start에서 tmp으로 옮기기(1->2) - 2^(n-1)-1 번 실행
  hanoi(n-1,start,tmp,end)
  #start 가장 위에 있는 원판을 end으로 옮기기(1->3) - 1번 실행
  print(start,end)
  #n-1개의 원판을 tmp에서 end로 옮기기(2->3) - 2^(n-1)-1 번 실행
  hanoi(n-1,tmp,end,start)

print(2**n-1)#옮긴 횟수
if n<=20:
  hanoi(n,1,3,2)