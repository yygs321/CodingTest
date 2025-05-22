def solution(n, results):
    answer = 0
    runners=[[[] for _ in range(2)] for _ in range(n+1)]
    
    for win,lose in results:
        runners[win][1].append(lose)
        runners[lose][0].append(win)

    print(runners)
    visited=[[False if i!=j else True for j in range(n+1)] for i in range(n+1)]
    for win, lose in runners:
        for w in win:
            for l in lose:
                if visited[w][l] and visited[l][w]:
                    continue
                visited[w][l]=True
                runners[w][1].append(l)
            #runners[w][1].extend(lose)
        for l in lose:
            for w in win:
                if visited[w][l] and visited[l][w]:
                    continue
                visited[l][w]=True
                runners[l][0].append(w)
                #            runners[l][0].extend(win)
            
    for win,lose in runners:
        if len(set(win+lose))>=n-1:
            answer+=1
    return answer