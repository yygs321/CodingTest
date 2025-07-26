def solution(scores):
    answer = 1
    if len(scores)==1:
        return answer
    
    wanho=scores[0]
    wanho_val=sum(wanho)
    
    new_scores=scores[1:]
    new_scores.sort(key=lambda x:(-x[0],x[1]))
    max_a,max_b=new_scores[0]
    
    for a,b in new_scores:
        if a>wanho[0] and b>wanho[1]:
            return -1
        if max_a>a and max_b>b:
            continue
        
        if a+b>wanho_val:
            answer+=1
            
        if b>max_b:
            max_a=a
            max_b=b

    
    return answer