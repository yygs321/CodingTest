from collections import defaultdict
n=int(input())
cat=list(input().rstrip())

tmp=defaultdict(int)
l,r=0,1
tmp[cat[l]] += 1
tmp[cat[r]] += 1
answer=0
while l<r and r<len(cat):

    if len(tmp)<=n:
        answer = max(answer, sum(tmp.values()))
        r+=1
        if r>=len(cat):
            break
        tmp[cat[r]] += 1
    else:
        tmp[cat[l]] -= 1
        if tmp[cat[l]]==0:
            del tmp[cat[l]]
        l+=1
print(answer)