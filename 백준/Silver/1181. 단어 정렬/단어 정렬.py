T=int(input())
ls=[]
for _ in range(T):
    ls.append(input())
ls=list(set(ls))
ls.sort(key= lambda x: (len(x), x))
for l in ls:
    print(l)