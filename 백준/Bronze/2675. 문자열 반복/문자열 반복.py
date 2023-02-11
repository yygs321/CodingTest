T=int(input())
for _ in range(T):
    m,st=input().split()
    result=""
    for s in st:
        result+=s*int(m)
    print(result)