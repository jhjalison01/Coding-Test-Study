def solution(n, cur, cmd):
    answer = ['O']*n
    
    table = {i: [i-1,i+1] for i in range(n)} #linked list로 사용
    table[0]=[None,1]
    table[n-1]=[n-2,None]
    stack=[]
    
    for c in cmd:
        #삭제
        if c == 'C':
            answer[cur]='X'
            prev,nxt=table[cur]
            stack.append([prev,cur,nxt])
            if nxt == None:
                cur=prev
            else:
                cur=nxt
                
            if nxt == None:
                table[prev][1]=None
            elif prev == None:
                table[nxt][0]=None
            else:
                table[prev][1]=nxt
                table[nxt][0]=prev
        #복구
        elif c=='Z':
            prev,now,nxt=stack.pop()
            answer[now]='O'
            if nxt == None:
                table[prev][1]=now
            elif prev==None:
                table[nxt][0]=now
            else:
                table[prev][1]=now
                table[nxt][0]=now
        #커서 이동
        else:
            c1,c2=c.split(" ")
            c2=int(c2)
            if c1 =="D":
                for _ in range(c2):
                    cur=table[cur][1]
            else:
                for _ in range(c2):
                    cur=table[cur][0]
                    
    return "".join(answer)