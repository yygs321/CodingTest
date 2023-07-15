from bisect import bisect_left

# 3명의 합이 3이 되도록
# start, mid, end
n = int(input())
students = list(map(int, input().split()))
students.sort()

answer = 0
# 3포인터
# 각 start의 경우에서 mid, end 구해보기
for start in range(n-2):
    mid = start+1
    end = n-1
    while mid < end:
        score = students[start]+students[mid]+students[end]

        if score == 0:
            #
            if students[mid] == students[end]:
                # 같은 수 개수만큼 더해주기
                answer += end-mid
            else:
                # 개수기 때문에 +1
                answer += end-bisect_left(students, students[end]) + 1
            # mid와 같은값의 경우는 mid가 이동하면서 찾을 것
            mid += 1
        elif score < 0:
            mid += 1
        else:
            end -= 1


print(answer)