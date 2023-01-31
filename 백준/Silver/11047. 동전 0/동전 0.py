n,k=map(int,input().split())
coin=[]
count=0
for i in range(n):
    c=int(input())
    coin.append(c)
    
for c in reversed(coin):    
    count+=k//c
    k%=c
    if k==0:
        break
        
                
print(count)