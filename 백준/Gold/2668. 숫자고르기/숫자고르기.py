N = int(input())			
lst=[0]
for _ in range(N):
    lst.append(int(input()))
answer = set()

# dfs 정의
def dfs(num):
    first.add(num)			
    second.add(lst[num])
  
    if lst[num] in first:	# 이어졌던 값 중 lst[num]이 있을 때
        if first == second:		# 첫번째 줄 집합과 두번째 줄 집합이 같으면 사이클
            answer.update(first)	# 결과 업데이트
            return True
          
        return False
    return dfs(lst[num])	# 두번째줄 값 이어서 탐색

# dfs 실행
for i in range(1, N+1):
    if i not in answer:		# 결과에 없을 경우만
        #집합 초기화
        first=set()
        second=set()
        dfs(i)

print(len(answer))
#리스트 한번에 출력하는 방법: print(*list)
print(*sorted(list(answer)), sep="\n")