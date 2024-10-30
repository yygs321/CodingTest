from collections import Counter

def solution(topping):
    answer = 0
    checked=set()
    count_lst=Counter(topping)
    
    for tp in topping:
        count_lst[tp]-=1
        if count_lst[tp]<=0:
            count_lst.pop(tp)
        
        if tp not in checked:
            checked.add(tp)
            
        if len(checked)==len(count_lst):
            answer+=1
        
    return answer