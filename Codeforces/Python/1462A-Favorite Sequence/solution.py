# https://codeforces.com/problemset/problem/1462/A

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    nums = list(input().split())

    left = 0
    right = len(nums) - 1
    original = []

    while left < right:
        original.append(nums[left])
        original.append(nums[right])

        left += 1
        right -= 1

    # When len(nums) is odd
    if left == right:
        original.append(nums[left])

    print(" ".join(original))
