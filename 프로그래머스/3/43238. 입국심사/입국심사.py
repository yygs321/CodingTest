def solution(n, times):
    answer = float('inf')
    
    max_time=max(times)*n
    l=0
    r=max_time
    while l<=r:
        mid=(l+r)//2
        cnt=0
        for t in times:
            cnt+=mid//t
        if cnt>=n:
            r=mid-1
            answer=min(answer,mid)
        else:
            l=mid+1
    
    return answer