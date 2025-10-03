from bisect import bisect_left

def solution(players, m, k):
    answer=0
    servers=[]
    
    for idx, player in enumerate(players):
        i=bisect_left(servers, idx)
        if i!=0:
            servers=servers[i:]
        
        if player<m:
            continue
            
        need=player//m
        if need>len(servers):
            plus=need-len(servers)
            answer+=plus 
            servers+=[idx+k-1 for _ in range(plus)]
        
    return answer