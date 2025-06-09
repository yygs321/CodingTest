from bisect import bisect_left
def solution(citations):
    answer = 0
    citations.sort()
    n=len(citations)
    l,r=0,10000
    while l<=r:
        mid=(l+r)//2
        idx=bisect_left(citations,mid)
        if n-idx>=mid:
            l=mid+1
            answer=max(answer,mid)   
        else:
            r=mid-1 
        
    return answer