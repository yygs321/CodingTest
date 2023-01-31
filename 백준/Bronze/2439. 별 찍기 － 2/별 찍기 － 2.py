#2349
T=int(input())
for i in range(1,T+1):
    if (T-i)>0:
        print(" "*(T-i-1),"*"*i)
    else:
        print("*"*i)