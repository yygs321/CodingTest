def solution(e, starts):
    answer = []
    nums=[0 for _ in range(e+1)]
    for i in range(1,(e+1)//2):
        for j in range(i,(e//i)+1):
            if i==j:
                nums[i*j]+=1
            else:
                nums[i*j]+=2
    
    last=1
    cnt=[]
    while last<=e:
        k=last+nums[last:e+1].index(max(nums[last:e+1]))
        cnt.append(k)
        last=k+1
        
    for start in starts:
        for i in range(len(cnt)):
            if start>cnt[i]:
                continue
            answer.append(cnt[i])
            break
    
    return answer