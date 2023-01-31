#10871(못푼 문제)
A,X =map(int,input().split())
lt1= list(map(int,input().split()))
lt2=[]
for i in range(0,A):
    if lt1[i]<X:
        lt2.append(lt1[i])
for i in lt2:
    print(i, end=' ')