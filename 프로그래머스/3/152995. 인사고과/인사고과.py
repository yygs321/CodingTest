def solution(scores):
    answer = 0
    wanho=scores[0]
    
    filtered=[]
    for score in scores[1:]:
        if sum(score)<=sum(wanho):
            continue
        filtered.append((-score[0], score[1]))
    filtered.sort()
    
        
    cnt=1
    max_b=0
    for a,b in filtered:
        a,b=-a,b
        
        if wanho[0]<a and wanho[1]<b:
            return -1
            
        if b<max_b:
            continue
        cnt+=1
        max_b=b
    
    answer=cnt
    return answer