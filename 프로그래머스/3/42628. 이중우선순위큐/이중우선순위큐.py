import heapq
def solution(operations):
    result = []
    
    for operation in operations:
        oper, val= operation.split()
        if oper=='I':
            heapq.heappush(result,int(val))
        elif oper=='D':
            if not result: continue
            if int(val)>=0:
                tmp=[-x for x in result]
                heapq.heapify(tmp)
                heapq.heappop(tmp)
                result=[-x for x in tmp]
                heapq.heapify(result)
            else:
                heapq.heappop(result)
    
    answer=[]
    if result:
        tmp=[-x for x in result]
        heapq.heapify(tmp)
        maxV=-heapq.heappop(tmp)
        minV=heapq.heappop(result)
        answer.append(maxV)
        answer.append(minV)
    else:
        answer.append(0)
        answer.append(0)
    return answer
