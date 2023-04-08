def perm(cnt,selectedIdx):
    global m
    if cnt==m:
        print(*result)
        return
  
    last=-1
    for i in range(len(lst)):
        if i in selectedIdx or last==lst[i]: continue
        result.append(lst[i])
        selectedIdx.append(i)
        last=lst[i]
        perm(cnt+1,selectedIdx)
        selectedIdx.pop()
        result.pop()


n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
selectedIdx=[]
result=[]
answer=[]

perm(0,selectedIdx)