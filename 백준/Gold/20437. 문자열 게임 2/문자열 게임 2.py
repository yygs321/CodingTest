from collections import defaultdict

#어떤 문자를 k개 포함하는 가장짧은 문자열 길이
#포함하고, 처음, 끝이 해당문자인 가장 긴 문자열

#defaultdict으로 해당 문자열을 key로,
#위치값을 value list로 넣는다
n=int(input())
for _ in range(n):
    wlist=list(input().rstrip())
    k=int(input())
    ans1, ans2=int(1e9),0
    
    wdict=defaultdict(list)
    for idx,w in enumerate(wlist):
        wdict[w].append(idx)

    for k1,v1 in wdict.items():
        if len(v1)>=k:
            for i in range(len(v1)-k+1):
                ans1=min(ans1,wdict[k1][i+k-1]-wdict[k1][i]+1)
                ans2=max(ans2,wdict[k1][i+k-1]-wdict[k1][i]+1)
    
    if ans1==int(1e9):
        print(-1)
    else:
        print(ans1, ans2)