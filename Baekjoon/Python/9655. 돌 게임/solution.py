# https://www.acmicpc.net/problem/9655


import sys

input = sys.stdin.readline

n = int(input())

dp = [0] + [1 for _ in range(n)]
for idx in range(2, n + 1):
    """
    끝이 0일땐 조건이 없으므로 idx - 1에서 끝이 1일땐 무조건 끝부분이 01이어야 하므로 idx - 2에서 가져온다"""
    dp[idx] = dp[idx - 1] + dp[idx - 2]
print(dp[n])
