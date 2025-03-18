from collections import defaultdict
def solution(n, info):
    answer =defaultdict(list)
    
    def dfs(cnt,tmp,idx):
        if cnt<=0:
            apeach=0
            lion=0
            for i,ab in enumerate(zip(info,tmp)):
                a,b=ab
                if a==0 and b==0:
                    continue
                if a>=b:
                    apeach+=(10-i)
                else:
                    lion+=(10-i)
                    
            if apeach>=lion:
                return
            else:
                answer[lion-apeach].append(list(reversed(tmp)))
                return
        
        if idx>10:
            return
        
        for k in range(cnt+1):
            tmp[idx]+=k
            dfs(cnt-k,tmp[:],idx+1)
            tmp[idx]-=k

        
    dfs(n,[0 for _ in range(11)],0)      
    
    #여러가지일 경우 가장 낮은 점수를 더 많이 맞힌 경우로 리턴
    #없을경우 [-1]
    if answer:
        maxKey=sorted(answer,reverse=True)[0]
        return list(reversed(sorted(answer[maxKey],reverse=True)[0]))
    else:
        return [-1]