
def solution(plans):
    plans.sort(key=lambda x:x[1])
    answer = []
    wait=[]
    
    for idx, plan in enumerate(plans):
        name, start, time=plan
        hh,mm=map(int,start.split(":"))
        start=hh*60+mm
        time=int(time)
        
        if idx==len(plans)-1:
            answer.append(name)
            break
        hh2,mm2=map(int,plans[idx+1][1].split(":"))
        next_start=hh2*60+mm2
        
        if start+time==next_start:
            answer.append(name)
        elif start+time>next_start:
            wait.append((name,(start+time)-next_start))
        else: #시간이 남으면
            answer.append(name)
            if not wait:
                continue
            remain=next_start-(start+time)
            while remain and wait:
                wait_name, wait_time=wait.pop()
                if remain>=wait_time:
                    answer.append(wait_name)
                    remain-=wait_time
                else:
                    wait.append((wait_name, wait_time-remain))
                    remain=0
    
    while wait:
        name,time=wait.pop()
        answer.append(name)
    
    return answer