#절댓값이 가장 큰 수가 되어야함
from itertools import permutations

def solution(expression):
    answer = 0
    n=len(expression)
    
    exp=[]
    flag=set()
    num=""
    for i, ep in enumerate(expression):
        if i==n-1:
            num+=ep
            exp.append(num)
        if ep.isdigit():
            num+=ep
            continue
        else:
            flag.add(ep)
            exp.append(num)
            exp.append(ep)
            num=""
    
    for perm in permutations(flag,len(flag)):
        tmp=exp[:]
        
        for p in perm:
            while p in tmp:
                idx=tmp.index(p)
                tmp[idx-1]=str(eval(''.join(tmp[idx-1:idx+2])))
                del tmp[idx:idx+2]
        
        answer=max(answer,abs(int(tmp[0])))
            
    return answer