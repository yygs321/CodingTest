from collections import deque
def solution(elements):
    
    result=set(elements)
    
    for i in range(1,len(elements)):
        queue=deque([], i+1)
        for j in range(-i,i+1):
            queue.append(elements[j])
            result.add(sum(queue))
    
    return len(list(result))