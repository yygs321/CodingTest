a,b,n,w=map(int,input().split())
result=[]
for i in range(1,n):
    if (a*i)+(b*(n-i))==w:
        result.append(i)

if len(result)>1 or not result:
    print(-1)
else:
    print(result[0], n-result[0])