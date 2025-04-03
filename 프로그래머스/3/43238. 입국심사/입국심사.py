def solution(n, times):
    answer = float('inf')
    
    time=(max(times)*n)//len(times)
    l=0
    r=time
    while l<=r:
        mid=(l+r)//2
        tmp=0
        for t in times:
            tmp+=mid//t
        if tmp>=n:
            r=mid-1
            answer=min(answer,mid)
        else:
            l=mid+1
    
    
    return answer