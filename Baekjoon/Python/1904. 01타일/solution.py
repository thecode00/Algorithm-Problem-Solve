# https://www.acmicpc.net/problem/1904


import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + [1 for _ in range(n)]

if n > 1:
    dp[2] = 2
for idx in range(3, n + 1):
    """
    00 타일을 붙이는경우: idx - 2, 1 타일을 붙이는경우: idx - 1
    """
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 15746
print(dp[n])
