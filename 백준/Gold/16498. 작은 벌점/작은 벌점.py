from collections import defaultdict

a, b, c = map(int, input().split())
alst = sorted(map(int, input().split()))
blst = sorted(map(int, input().split()))
clst = sorted(map(int, input().split()))

idx_dict = defaultdict(int)
answer = float('inf')

while idx_dict[0] < a and idx_dict[1] < b and idx_dict[2] < c:
    tmp = [alst[idx_dict[0]], blst[idx_dict[1]], clst[idx_dict[2]]]
    minV = min(tmp)
    maxV = max(tmp)
    min_idx = tmp.index(minV)

    answer = min(answer, maxV - minV)

    idx_dict[min_idx] += 1

print(answer)