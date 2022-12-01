# https://www.acmicpc.net/problem/11726


import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + [1 for _ in range(n)]
if n > 1:
    dp[2] = 2
for idx in range(3, n + 1):
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 10007
print(dp[n])
