def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x,y=ball
        diffX = startX-x
        diffY = startY-y
        
        left = (startX+x)**2 + (diffY**2)          # 왼쪽 쿠션
        right = ((m-startX)+(m-x))**2 + (diffY**2) # 오른쪽 쿠션
        top = (diffX**2) + ((n-startY)+(n-y))**2   # 위쪽 쿠션
        bottom = (diffX**2) + (startY+y)**2        # 아래쪽 쿠션
        
        if diffX == 0: # X축 같은 선상일 때
            if diffY > 0: # 아래쪽 방향 쿠션 안됨
                res = min(left, right, top)        
            else : # 위쪽 방향 쿠션 안됨
                res = min(left, right, bottom)    
                
        elif diffY == 0: # Y축 같은 선상일 때
            if diffX > 0: # 왼쪽 쿠션 안됨
                res = min(right, top, bottom)        
            else : # 오른쪽 쿠션 안됨
                res = min(left, top, bottom)      
                
        else: # 같은 축 없을 때
            res = min(left, right, top, bottom)
            
        answer.append(res)
    return answer