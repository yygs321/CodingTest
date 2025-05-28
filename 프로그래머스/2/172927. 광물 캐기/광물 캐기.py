# 5번 캐고나면 끝
from itertools import permutations
from collections import defaultdict, Counter

def solution(picks, minerals):
    answer = 0
    n=len(minerals)
    m=sum(picks)
    
    pick=['diamond', 'iron', 'stone']
    picks_dict=defaultdict(int)
    picks_total=[]
    for idx,cnt in enumerate(picks):
        picks_dict[pick[idx]]=idx
        picks_total+=[idx]*cnt
    
    minerals_cnt=[]
    
    for i in range(n):
        minerals[i]=pick.index(minerals[i])
    
    for i in range(0,n,5):
        cnt_lst=list(Counter(minerals[i:i+5]).items())
        cnt_lst.sort()
        minerals_cnt.append(cnt_lst)
    
    if m>=(n-1)//5+1:
        minerals_cnt.sort(key=lambda x:[(x[i][0],-x[i][1]) for i in range(len(x))])
    
        for mineral in minerals_cnt:
            p=-1
            for idx,pick in enumerate(picks):
                if pick:
                    p=idx
                    picks[idx]-=1
                    break
            if p==-1:
                break

            for mn in mineral:
                if p-mn[0]<=0:
                    answer+=1*mn[1]
                else:
                    answer+=(5**(p-mn[0]))*mn[1]
            
    else:
        answer=100000000
        for perm in set(permutations(picks_total,m)):
            tmp=0
            for idx,mineral in enumerate(minerals_cnt):
                if idx>=len(perm):
                    break

                for mn in mineral:
                    if perm[idx]-mn[0]<=0:
                        tmp+=1*mn[1]
                    else:
                        tmp+=(5**(perm[idx]-mn[0]))*mn[1]
            answer=min(answer,tmp)

    return answer
