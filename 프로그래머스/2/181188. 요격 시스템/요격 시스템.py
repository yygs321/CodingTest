def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    
    i = -1
    e = 0
    
    while i < len(targets) - 1:
        i += 1
        
        if targets[i][0] >= e:
            answer += 1
            e = targets[i][1]
    
    return answer
