def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    i=-1
    while i<len(targets)-1:
        i+=1
        target=targets[i]
        
        while i+1<len(targets) and target[1]>targets[i+1][0]:
            i+=1
        answer+=1
    
    return answer