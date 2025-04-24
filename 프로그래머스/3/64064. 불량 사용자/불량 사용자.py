def solution(user_id, banned_id):
    answer = set()
    result=[]
    
    for bann in banned_id:
        tmp=set()
        for user in user_id:
            if len(bann)!=len(user):
                continue
            for b,u in zip(bann,user):
                if b=='*':
                    continue
                if b!=u:
                    break
            else:
                tmp.add(user)
        result.append(tmp)
    
    def dfs(depth, selected):
        nonlocal answer
        if depth == len(banned_id):
            answer.add(tuple(sorted(selected)))
            return
        
        for user in result[depth]:
            if user not in selected:
                selected.append(user)
                dfs(depth + 1, selected)
                selected.pop()
    dfs(0,[])

    return len(answer)