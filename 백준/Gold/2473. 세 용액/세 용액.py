n=int(input())
lst=list(sorted(map(int,input().split())))
minV=float('inf')
answer=[]
flag=0

for i in range(n-2):
    l=i+1
    r=n-1

    while l<r:
        tmp=[lst[i],lst[l],lst[r]]
        if abs(sum(tmp)) <= minV:
            answer=tmp
            minV=abs(sum(tmp))

        if sum(tmp)<0:
            l+=1
        elif sum(tmp)>0:
            r-=1
        else:
            answer=tmp
            flag=1
            break

    if flag:
        break

print(*answer)