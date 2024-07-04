def solution(routes):
    routes.sort(key=lambda x:x[1])
    tmp=routes[0][1]
    
    answer = 1
    for idx,route in enumerate(routes):
        if idx==0: continue
        if route[0]>tmp:
            answer+=1
            tmp=route[1]

    return answer