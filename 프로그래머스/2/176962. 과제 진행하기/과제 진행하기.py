def solution(plans):
    answer = []
    n=len(plans)
    start_time=[]
    dic={}
    for idx,plan in enumerate(plans):
        name, start, playtime=plan
        hh,mm=map(int,start.split(":"))
        hhmm=hh*60+mm
        start_time.append((hhmm, idx, int(playtime)))
        dic[idx]=name

    start_time.sort(key=lambda x:x[0])
    
    remain=[]
    while start_time:
        start, idx, play= start_time.pop(0)
        if not start_time:
            answer.append(dic[idx])
            continue
            
        nxt=start_time[0][0]
        if start+play>nxt:
            remain.append([idx, (start+play)-nxt])
        elif start+play==nxt:
            answer.append(dic[idx])
        else:
            answer.append(dic[idx])
            tmp=nxt-(start+play)
            while remain and tmp:
                if remain[-1][1] <= tmp:
                    tmp-=remain[-1][1]
                    answer.append(dic[remain.pop()[0]])
                else:
                    remain[-1][1]-=tmp
                    break
        
    while remain:
        idx,play=remain.pop()
        answer.append(dic[idx])
        
    return answer