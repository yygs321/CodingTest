import heapq
def solution(n, works):
    #피로도: 시작 시점+(남은일의 작업량)**2
    answer = 0
    queue=[]
    for work in works:
        heapq.heappush(queue,-work)
    while n>=1:
        if not queue:
            break
        tmp=heapq.heappop(queue)
        if tmp!=0:
            heapq.heappush(queue, tmp+1)
        n-=1
    
    for q in queue:
        if q==0:
            continue
        answer+=q**2
    return answer