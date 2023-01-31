def func(N):
    a=N//10
    b=N%10
    c=(a+b)%10 
    d=b*10 +c
    return d

N=int(input())
tmp=N
cnt=1

while N !=func(tmp):
    cnt +=1
    tmp=func(tmp)

print(cnt)