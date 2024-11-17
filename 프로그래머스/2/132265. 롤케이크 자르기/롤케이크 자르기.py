from collections import Counter

def solution(topping):
    answer = 0
    dict_cnt=Counter(topping)
    n=len(set(topping))
    
    m=0
    set1=set()
    for t in topping:
        if t not in set1:
            m+=1
            set1.add(t)
        dict_cnt[t]-=1
        
        if dict_cnt[t]<=0:
            n-=1
        
        if n==m:
            answer+=1
        
        
    return answer