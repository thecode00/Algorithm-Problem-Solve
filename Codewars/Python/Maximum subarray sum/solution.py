# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# Time complexity: O(N)

def max_sequence(arr):
    if not arr:
        return 0
    sum_dp = [0 for _ in range(len(arr))]
    for idx in range(len(arr)):
        sum_dp[idx] = max(sum_dp[idx - 1] + arr[idx], arr[idx])
    max_sum = max(sum_dp)
    return max_sum if max_sum >= 0 else 0


def max_sequence(arr):
    max_sum = cur_sum = 0
    for num in arr:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(max_sum, cur_sum)
    return max_sum
