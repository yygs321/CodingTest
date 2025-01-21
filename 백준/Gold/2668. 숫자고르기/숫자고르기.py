n=int(input())
lst=[0]+[int(input()) for _ in range(n)]
answer=[]

def dfs(val):
    global answer
    if val in picked:
        i=picked.index(val)
        answer+=picked[i:]
        return

    picked.append(val)
    dfs(lst[val])
    return

for idx, val in enumerate(lst):
    if idx==0: continue
    if idx in answer or val in answer: continue
    picked = []
    picked.append(idx)
    dfs(val)

answer=list(set(answer))
print(len(answer))
print(*sorted(answer), sep='\n')