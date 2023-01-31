#2742
A=int(input())
lt1=list()
i=0
for i in range(0,A):
    i=i+1
    lt1.append(i)
lt1.sort(reverse=True)
j=0
for j in range(0,A):
    print(lt1[j])
    
    