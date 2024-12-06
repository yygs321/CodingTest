from bisect import bisect_left
def solution(A, B):
    A.sort()
    B.sort()
    cnt=0
    for idx in range(len(B)):
        bi=bisect_left(A,B[idx])
        if bi>0:
            A.pop(0)
            cnt+=1
            
    return cnt