def solution(points, routes):
    answer=0
    move_dict={}
    for route in routes:
        time=0
        sx,sy=0,0
        for idx, point_num in enumerate(route[:-1]):
            sx,sy=points[point_num-1]
            ex,ey=points[route[idx+1]-1]
            
            while True:
                if sx==ex and sy==ey:
                    break 
                if (sx,sy,time) in move_dict:
                    move_dict[(sx,sy,time)]+=1
                else:
                    move_dict[(sx,sy,time)]=1
                time+=1

                if ex>sx: 
                    sx+=1
                elif ex<sx:
                    sx-=1
                else:
                    if ey>sy:
                        sy+=1
                    elif ey<sy:
                        sy-=1
        # 맨마지막 위치가 안담겼기때문에 담아주기
        if (sx,sy,time) in move_dict:
            move_dict[(sx,sy,time)]+=1
        else:
            move_dict[(sx,sy,time)]=1
        
    for val in list(move_dict.values()):
        if val>=2:
            answer+=1
            
    return answer