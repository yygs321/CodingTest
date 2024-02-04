def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    
    for i in range(n): # 방향     
        for j in range(i, n):            
            if i % 3 == 0: # 하                
                x += 1
            elif i % 3 == 1: # 우                
                y += 1
            else: # 상                
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    #sum(덧셈할 것, 처음에 더할 것) = 더한 값이 나옴
    # sum([[1,2],[3,4,5]], []) -> [] + [1,2] + [3,4,5] = [1,2,3,4,5] 
    return sum(answer, [])