#11,22,..
#2자리수 다되고 1~99
#111,123, 135, 147,159, 210(-1)
from collections import deque

n=int(input())
if n<100:
    lst=set([i for i in range(1,n+1)])
else:
    lst = set([i for i in range(1, 100)])

k=100
while k<=n:
    l = len(str(k))
    strk=list(str(k))
    minusk=list(str(k))
    for j in range(5):
        flag=1
        for i in range(l-1):
            strk[i+1]=str(int(strk[i])+j)
            if int(minusk[i]) - j <0:
                flag=0
            minusk[i + 1] = str(int(minusk[i]) - j)
        intk=int(''.join(strk))
        if intk<=n and intk not in lst:
            lst.add(intk)
        if flag==0: continue
        intk2 = int(''.join(minusk))
        if intk2<=n and intk2 not in lst:
            lst.add(intk2)


    k+=10**(l-1)

print(len(lst))