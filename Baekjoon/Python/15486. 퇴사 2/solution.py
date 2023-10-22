# https://www.acmicpc.net/problem/15486


import sys

input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for idx in range(1, n + 1):
    t, p = schedule[idx - 1]
    t -= 1
    dp[idx] = max(dp[idx], dp[idx - 1])
    if idx + t > n:
        continue
    dp[idx + t] = max(dp[idx - 1] + p, dp[idx + t])
print(dp[n])
