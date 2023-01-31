#4344 (정답)
n=int(input())
for i in range(n):
    A= list(map(int,input().split()))
    average=float(sum(A[1:]))/float(A[0])
    count=0
    for j in A[1:]:
        if j>average:
            count +=1
    print("%0.3f%%"%round((float(count)/float(A[0])*100),3))