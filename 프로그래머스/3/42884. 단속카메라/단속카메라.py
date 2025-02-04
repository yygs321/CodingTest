def solution(routes):
    cnt = 0
    routes.sort(key=lambda x:x[1])
    last=-30001

    for idx, route in enumerate(routes):
        if idx==0:
            cnt+=1
            last=route[1]
            continue
        if last<route[0]:
            cnt+=1
            last=route[1]
    return cnt