import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    indict=defaultdict(list)
    outdict=defaultdict(list)
    cars=[]
    for record in records:
        time,carN,inout=record.split()
        hh,mm=map(int,time.split(":"))
        time=(hh*60)+mm
        
        if inout=='IN':
            indict[carN].append(time)
            cars.append(carN)
        else:
            outdict[carN].append(time)

    result=defaultdict(int)
    for car in sorted(cars):
        intime=indict[car].pop(0)
        if outdict[car]:
            outtime=outdict[car].pop(0)
        else:
            outtime=(23*60)+59
    
        diff=outtime-intime
        result[car]+=diff
    
    print(result)
    for key in sorted(result.keys()):
        r=result[key]
        if r<=fees[0]:
            answer.append(fees[1])
            continue
        
        tmp=fees[1]
        r-=fees[0]
        tmp+=math.ceil(r/fees[2])*fees[3]
        
        answer.append(tmp)
        
    return answer