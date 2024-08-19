n=int(input())

cnt=0
for a in range(1,501):
    for b in range(a,501):
        if abs((a+b)*(a-b))==n:
            cnt+=1

print(cnt)