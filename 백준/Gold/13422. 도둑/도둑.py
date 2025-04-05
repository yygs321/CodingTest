t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    village=[0]+list(map(int,input().split()))

    prefix_sum=village[:]
    for i in range(1,m):
        prefix_sum.append(village[i])

    for i in range(1,n+m):
        prefix_sum[i]+=prefix_sum[i-1]

    answer=0
    for i in range(m,n+m):
        if prefix_sum[i]-prefix_sum[i-m]>=k:
            continue
        answer+=1

    if n==m:
        print(1 if sum(village)<k else 0)
    else:
        print(answer)