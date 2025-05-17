

import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    nums = sorted(map(int, input().split()))
    is_ok = all(nums[idx + 1] - nums[idx] <= 1 for idx in range(n - 1))

    print("YES" if is_ok else "NO")
