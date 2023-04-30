#n일까지 완료되지 못하는 상담은 시작 x
n=int(input())
time=[]
amount=[]
d=[0]*(n+1)


for i in range(n):
    t,p=map(int,input().split())
    time.append(t)
    amount.append(p)

for i in range(n):
    #완료되는 시점이 n+1보다 넘어가면 for문 돌지 않음
    for j in range(i+time[i],n+1): 
        if d[j] < d[i]+amount[i]:
            d[j]=d[i]+amount[i]

print(d[n])