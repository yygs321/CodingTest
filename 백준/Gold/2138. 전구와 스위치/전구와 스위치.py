n=int(input())
start=list(map(int,input().rstrip()))
end=list(map(int,input().rstrip()))
val=[0,1]
def count():
    result=0
    tmp=start[:]

    for i in range(1,n):
        if tmp[i-1]==end[i-1]:
            continue

        tmp[i-1]=val[(tmp[i-1]+1)%2]
        tmp[i]=val[(tmp[i]+1)%2]
        if i+1<n:
            tmp[i+1]=val[(tmp[i+1]+1)%2]
        result+=1

    if tmp==end: return result
    else: return int(1e9)

#전구 스위치 안 누른 경우
answer=count()

#전구 스위치 누른 경우
start[0]=val[(start[0]+1)%2]
start[1]=val[(start[1]+1)%2]
answer=min(answer, count()+1)

if answer==int(1e9):
    print(-1)
else:
    print(answer)