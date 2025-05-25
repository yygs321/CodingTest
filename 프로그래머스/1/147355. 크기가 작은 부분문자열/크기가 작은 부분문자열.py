def solution(t, p):
    n=len(p)
    answer = 0
    point=0
    
    while point<=len(t)-n:
        if int(t[point:point+n])<=int(p):
            answer+=1
        point+=1
    return answer