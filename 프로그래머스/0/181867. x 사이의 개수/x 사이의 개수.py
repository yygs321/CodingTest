def solution(myString):
    tmp=list(myString.split('x'))
    answer=[len(x) for x in tmp]
    return answer