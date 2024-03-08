from itertools import combinations as combi
def solution(relation):
    result=[]
    n=len(relation[0])
    num=[i for i in range(n)]
    remove=[]
    

    for k in range(1, n+1):
        for comb in combi(num,k):
            lst=[]
            for i in range(len(relation)):
                tmp=[]
                for c in comb:
                    tmp.append(relation[i][c])
                if tmp in lst:
                    break
                lst.append(tmp)

            else:
                for r in remove:
                    for x in range(1,len(comb)+1):
                        if r in list(combi(comb,x)):
                            break
                    else:
                        continue
                    break
                else:
                    remove.append(comb)

    print(remove)
    return len(remove)