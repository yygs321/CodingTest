from collections import deque
def solution(want, number, discount):
    answer = 0
    queue=deque()
    dic={}
    for w,n in zip(want,number):
        dic[w]=n
    
    
    for idx,dc in enumerate(discount):
        q=''
        if len(queue)>=10:
            q=queue.popleft()
        queue.append(dc)
        if q in list(dic.keys()):
            dic[q]+=1
        if dc in list(dic.keys()):
            dic[dc]-=1
            
        if len(set(dic.values()))==1 and list(dic.values())[0]==0:
            answer+=1
    
    return answer