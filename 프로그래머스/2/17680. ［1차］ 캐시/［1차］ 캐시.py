def solution(cacheSize, cities):
    lst=[]
    answer = 0
    if cacheSize==0:
        return 5*len(cities)
    
    for city in cities:
        city=city.lower()
        if city in lst:
            idx=lst.index(city)
            del lst[idx]
            lst.append(city)
            answer+=1
        else:
            if len(lst)>=cacheSize:
                lst.pop(0)
            answer+=5
            lst.append(city)
        
    
    return answer