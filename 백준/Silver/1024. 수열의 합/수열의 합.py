import sys
input=sys.stdin.readline

n,l= map(int,input().split())
for i in range(l,101): #길이가 l이상이어야 하므로
    x=n-(i*(i+1)/2)
    if x%i==0: #정수이면
        x=int(x/i) #길이로 나눈값까지가 x
        
        if x>=-1: #x+1부터 정수 여야함
            for j in range(1,i+1): #여기서 i가 l인것
                print(x+j, end=" ")
            print()
            break
        
else:
    print(-1)