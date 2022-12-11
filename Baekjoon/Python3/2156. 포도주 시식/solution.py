# https://www.acmicpc.net/problem/2156


import sys

input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for idx in range(1, n + 1):
    if idx <= 2:
        dp[idx] = dp[idx - 1] + wine[idx]
        continue
    """
    3가지 경우의수
    idx번째 잔을 마시고 idx - 1번째 잔도 마신경우: dp[idx - 3] + wine[idx - 1] + wine[idx]
    idx번째 잔만 마신경우: dp[idx - 2] + wine[idx]
    idx번째 잔을 3잔 연속룰 때문에 못마시는 경우: dp[idx - 1]"""
    dp[idx] = max(dp[idx - 1], dp[idx - 2] + wine[idx], dp[idx - 3] + wine[idx - 1] + wine[idx])
print(dp[n])
