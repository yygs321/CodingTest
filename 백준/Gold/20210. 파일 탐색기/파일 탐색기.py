import sys
from functools import cmp_to_key

def parse(s):
    res, i = [], 0
    while i < len(s):
        if s[i].isalpha():
            res.append(s[i])
            i += 1
        else:
            num = ''
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            res.append(num)
    return res

def natural_sort(s1, s2):
    p1, p2 = parse(s1), parse(s2)
    for a, b in zip(p1, p2):
        if a == b:
            continue
        if a.isdigit() and b.isalpha():
            return -1
        if a.isalpha() and b.isdigit():
            return 1
        if a.isalpha() and b.isalpha():
            return (a.lower() > b.lower()) - (a.lower() < b.lower()) or (a > b) - (a < b)
        if a.isdigit() and b.isdigit():
            return (int(a) > int(b)) - (int(a) < int(b)) or (len(a) > len(b)) - (len(a) < len(b))
    return len(p1) - len(p2)

lst = [input().strip() for _ in range(int(input()))]
print('\n'.join(sorted(lst, key=cmp_to_key(natural_sort))))