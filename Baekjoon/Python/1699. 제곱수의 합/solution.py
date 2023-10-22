"""
https://www.acmicpc.net/problem/1699
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [num for num in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        # if는 조건이 안되면 바로 넘기지만 min은 다 계산하기때문에 시간초과가 남
        # dp[i] = min(dp[i], dp[i - j * j] + 1)
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[n])
