answer=0
def dfs(numbers,target,idx,tmp):
    global answer
    if idx==len(numbers):
        if tmp==target: 
            answer+=1
            return True
        else: return

    dfs(numbers,target,idx+1,tmp+numbers[idx])
    dfs(numbers,target,idx+1,tmp-numbers[idx])
    

def solution(numbers, target):
    global answer    
    dfs(numbers,target,0,0)
    
    return answer