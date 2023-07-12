n,l=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort()
result=1
tmp=l-1
for i in range(1,n):
    tmp-=lst[i]-lst[i-1]

    if tmp<0: 
        result+=1
        tmp=l-1


print(result)
