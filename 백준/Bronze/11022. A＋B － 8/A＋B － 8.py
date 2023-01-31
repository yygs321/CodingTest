#11022
T = int(input())
i=0
for i in range(0,T):
    i +=1
    A,B=map(int,input().split())
    C=A+B
    print("Case #%d: %d + %d = %d"%(i,A,B,C))