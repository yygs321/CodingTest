# 물뿌리개 2개
# 1,2 동시에 사용, 나무 없으면 사용 불가
# 두개를 한나무에 사용가능 3
# 사과나무 개수
n = int(input())
# 원하는 나무 높이
trees = list(map(int, input().split()))


cnt = 0
for idx, tree in enumerate(trees):
    trees[idx] = tree % 2
    cnt += tree//2

if cnt < sum(trees):
    print("NO")
else:
    if (cnt-sum(trees)) % 3 == 0:
        print("YES")
    else:
        print("NO")