def solution(s):
    answer=0
    def length_check(n):
        if n < 2:
            return 0
        elif n < 10:
            return 1
        elif n < 100:
            return 2
        elif n<1000:
            return 3
        return 4

    def compress(s):
        n = len(s)
        if n <= 1:
            return n

        min_length = n

        for size in range(1, n // 2 + 1):
            compressed = 0
            prev = s[:size]
            count = 1

            for i in range(size, n, size):
                curr = s[i:i + size]

                if curr == prev:
                    count += 1
                else:
                    compressed += length_check(count) + size
                    prev = curr
                    count = 1

            # 마지막 남은 부분 처리
            compressed += length_check(count) + len(prev)

            min_length = min(min_length, compressed)
            
        return min_length
    
    answer=compress(s)
    return answer