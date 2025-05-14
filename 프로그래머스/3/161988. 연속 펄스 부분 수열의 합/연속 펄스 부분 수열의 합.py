def solution(sequence):
    n = len(sequence)
    
    pulse1 = [sequence[i] * (1 if i % 2 == 0 else -1) for i in range(n)]
    pulse2 = [sequence[i] * (-1 if i % 2 == 0 else 1) for i in range(n)]

    def max_subarray(arr):
        max_sum = curr_sum = arr[0]
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    return max(max_subarray(pulse1), max_subarray(pulse2))