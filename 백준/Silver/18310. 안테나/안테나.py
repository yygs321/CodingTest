n=int(input())
lst=list(map(int,input().split()))
lst.sort()

#개수가 홀수개여도 중간값 2개 다 거리계산하면 동일하기때문에 둘다 상관X
#아래 코드는 홀수일때 len(lst)//2 가 이미 중간값이기 때문에 오답
#print(lst[len(lst)//2-1])

#인덱스 맞추려면 1개빼고 //2
print(lst[(len(lst)-1)//2])