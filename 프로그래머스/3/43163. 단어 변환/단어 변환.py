answer = 10000
def solution(begin, target, words):
    visited=[False for _ in range(len(words))]
    
    def recur(cur, target,cnt):
        global answer
        if cur==target:
            answer=min(answer,cnt)
            return
        
        for idx, next in enumerate(words):
            if visited[idx]==True:
                continue
            # if len(set(cur+next))!=len(target)+1: #한글자 차이가 아니면
            #     continue
            # -> 	"aab", "aba"와 같이 중복된 글자가 다른글자일 경우 제외해버림
            flag=0
            for aval,bval in zip(cur,next):
                if aval!=bval:
                    flag+=1
            if flag>1:
                continue
            
            visited[idx]=True
            recur(next, target, cnt+1)
            visited[idx]=False
            
    recur(begin, target, 0)   
    
    if answer==10000:
        return 0
    else:
        return answer