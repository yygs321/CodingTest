n=int(input())

answer=0
candy=[0,0,0] #T, Y, N
def perm(cnt,tmp):
    global answer
    global n
    if cnt==3:
        if sum(candy)!=n:
            return
        if 0 in candy:
            return
        if candy[2]<candy[1]+2:
            return
        if candy[0]%2!=0:
            return
        answer+=1
        return
    
    if n-tmp<=0:
        return
    for i in range(1,n-tmp+1):
        candy[cnt]=i
        perm(cnt+1, tmp+i)
        candy[cnt]=0

perm(0,0)
print(answer)