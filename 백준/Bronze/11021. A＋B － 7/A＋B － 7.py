#11021
A=int(input())
i=0
for i in range(0,A):
    i=i+1
    B,C= map(int,input().split())
    print("Case #%d: %d"%(i,(B+C)))