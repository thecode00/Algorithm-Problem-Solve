"""
https://codeforces.com/problemset/problem/189/A
Time complexity: O(3N)
"""

import sys

input = sys.stdin.readline

n, a, b, c = map(int, input().split())
ribbon_lens = [a, b, c]
dp = [0] + [float("-inf")] * n  # Initialize dp list

for idx in range(1, n + 1):
    for len in ribbon_lens:
        if idx - len >= 0:  # When idx - len < 0 it will dp end of dp list
            dp[idx] = max(dp[idx], dp[idx - len] + 1)
print(dp[-1])
