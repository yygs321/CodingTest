from collections import Counter
from itertools import combinations, product

def solution(dice):
    answer = []
    n=len(dice)
    
    idx_comb_list=[list(idx_comb) for idx_comb in combinations(range(len(dice)),n//2)]
    #comb_team=[comb_set for comb_set in map(list,combinations(idx_comb_list,2)) if len(comb_set[0])*2==len(set(comb_set[0]+comb_set[1]))]
    
    cnt=0
    for a in idx_comb_list:
        b = [i for i in range(n) if i not in a]
        teamA=[]
        teamB=[]
        
        for i in a:
            teamA.append(dice[i])
        
        for i in b:
            teamB.append(dice[i])
        
        
        sumA=[sum(prod) for prod in product(*teamA)]
        sumB=[sum(prod) for prod in product(*teamB)]
        
        counterA=Counter(sumA)
        counterB=Counter(sumB)
        
        keysA=list(sorted(counterA.keys()))
        keysB=list(sorted(counterB.keys()))
        
        tmpA=0
        for i in keysA:
            for j in keysB:
                if i<=j:
                    break
                tmpA+=counterA[i]*counterB[j]
        tmpB=0
        for i in keysB:
            for j in keysA:
                if i<=j:
                    break
                tmpB+=counterB[i]*counterA[j]
                
        if cnt<tmpA:
            if tmpA<tmpB:
                cnt=tmpB
                answer=[x+1 for x in b]
            else:
                cnt=tmpA
                answer=[x+1 for x in a]
                
    return answer