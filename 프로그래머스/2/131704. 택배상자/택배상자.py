def solution(order):
    stack=[i for i in range(1,order[0]+1)]
    idx=0
    cur=order[0]
    while cur<=len(order) and idx<=len(order):
        if not stack:
            cur+=1
            stack.append(cur)
            continue
        
        if stack[-1]>=order[idx]:
            if stack[-1]-order[idx]>=1:
                break
            else:
                stack.pop()
                idx+=1
        else:
            cur+=1
            stack.append(cur)
            continue
            
    
    return idx
            