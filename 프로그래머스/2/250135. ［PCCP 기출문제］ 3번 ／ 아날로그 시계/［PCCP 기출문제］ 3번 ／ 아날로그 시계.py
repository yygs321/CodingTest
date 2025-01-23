def solution(h1, m1, s1, h2, m2, s2):
    
    answer = 0
    mcount, hcount = 0,0
    second1 = h1*60*60 + m1*60 + s1
    second2 = h2*60*60 + m2*60 + s2
    
    #넘기는 횟수를 세기때문에 시작시간 정각인 경우 따로 더해줌 
    if second1 == 0 or second1 == 60*60*12 :
        answer += 1
    
    for i in range(second1, second2) :
        '''
        숫자 간격마다 360도/12 = 30도
        - 시침: 1시간(3600초) 당 30도 -> 1초 당 30/3600= 1/120도
        - 분침: 5분(5*60초)당 30도 -> 1분 당 6도 -> 1초 당 6/60= 1/10도
        - 초침: 5초당 30 도 -> 1초당 6도
        '''
        # i초에 시,분,초침이 움직인 각도 (360를 넘지 않도록 나눔)
        s = (i*6)%360
        m = (i/10)%360
        h = (i/120)%360

        # i+1초 뒤 각도
        # 0도를 360도로 바꾼 이유는 359도랑 비교했을 때 한바퀴임을 명시하려고
        ns = 360 if (i+1)*6%360 == 0 else (i+1)*6%360
        nm = 360 if (i+1)/10%360 == 0 else (i+1)/10%360
        nh = 360 if (i+1)/120%360 == 0 else (i+1)/120%360
        
        if s < h and ns >= nh :
            hcount += 1
        if s < m and ns >= nm :
            mcount += 1
            
        # 시,분,침이 같은 경우 두번 더해지는 것을 방지하기 위해 한번 빼기
        if ns==nm==nh :
            answer -= 1
            
    answer += mcount + hcount
    
    return answer