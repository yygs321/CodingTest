from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    a,b=max(arrayA), max(arrayB)
    for ar, br in zip(arrayA,arrayB):
        a=gcd(a,ar)
        b=gcd(b,br)

    for ar, br in zip(arrayA,arrayB):
        if br%a==0:
            a=1
        if ar%b==0:
            b=1

    answer=max(a,b)
    if answer==1:
        answer=0
    
    return answer