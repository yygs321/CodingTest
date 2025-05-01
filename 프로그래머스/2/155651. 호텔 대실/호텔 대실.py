import heapq

def solution(book_time):
    time=[]
    for bk in book_time:
        sh,sm=map(int,bk[0].split(":"))
        eh,em=map(int,bk[1].split(":"))
        heapq.heappush(time, (sh*60+sm,eh*60+em))
        
    result=[]
    heapq.heappush(result,0)
    cnt=1
    while time:
        s,e=heapq.heappop(time)
        
        x=heapq.heappop(result)
        if x<=s:
            heapq.heappush(result,e+10)
        else:
            heapq.heappush(result,x)
            cnt+=1
            heapq.heappush(result,e+10)
            
    return cnt