def solution(distance, rocks, n):
    l,r=0,distance
    rocks.append(distance)
    rocks.sort()
    answer=0
    
    
    while l<=r:
        cur=0
        remove_cnt=0
        mid=(l+r)//2
        minV=float('inf')
        
        for rock in rocks:
            if rock-cur < mid:
                remove_cnt+=1
            else:
                minV=min(minV, rock-cur)
                cur=rock
            
        if remove_cnt>n:
            r=mid-1
        else:
            answer=minV
            l=mid+1
                
    return answer