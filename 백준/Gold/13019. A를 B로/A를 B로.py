#두 문자열이 같은 문자로 이루어져 있어야함
#글자수가 1이면 시작부터 같지 않은 한 영영 같아질 수 없음
A = input().strip()
B = input().strip()
n=len(A)
ans = 0

if sorted(A) != sorted(B):
    print(-1)
    exit()

if n==1:
    if A == B:
        print(0)
    else:
        print(-1)
    exit()

for i in range(len(A)-1,-1,-1):
    if A[i] != B[n-1]: # 뒤에서부터 비교해서 다르면 
        ans += 1
    else:
        if n>=0:
            n -= 1 #하나씩 앞당겨가면서 비교
print(ans)