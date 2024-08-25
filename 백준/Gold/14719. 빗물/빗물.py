h,w=map(int,input().split())
lst=list(map(int,input().split()))
max_value=max(lst)
max_idx=lst.index(max_value)

tmp=0
ans=0
for i in range(1,max_idx+1):
    if tmp==-1:
        if lst[i]<lst[i-1]:
            tmp=i-1
        else:
            tmp=i
        continue
    if lst[tmp]<=lst[i]:
        for j in range(tmp, i):
            ans+=lst[tmp]-lst[j]
        tmp=-1
    

tmp=w-1
for i in range(w-2, max_idx-1,-1):
    if tmp==-1:
        if lst[i]<lst[i+1]:
            tmp=i+1
        else:
            tmp=i
        continue
    if lst[tmp]<=lst[i]:
        for j in range(i+1,tmp):
            ans+=lst[tmp]-lst[j]
        tmp=-1

print(ans)