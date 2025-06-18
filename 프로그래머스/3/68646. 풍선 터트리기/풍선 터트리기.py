def solution(a):
    answer = 0
    n=len(a)
    left=a[:]
    for i in range(1,n):
        left[i]=min(left[i-1],a[i])
    right=a[:]
    for i in range(n-2,-1,-1):
        right[i]=min(right[i+1],a[i])
    
    for idx,cur in enumerate(a):
        if idx==0 or idx==n-1:
            answer+=1 #양끝은 무조건 남을 수 있음
            continue
        if left[idx-1]<cur and right[idx+1]<cur:
            continue
        answer+=1
        
    return answer