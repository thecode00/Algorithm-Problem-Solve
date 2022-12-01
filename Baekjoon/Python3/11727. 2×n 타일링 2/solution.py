# https://www.acmicpc.net/problem/11727


import sys

input = sys.stdin.readline

n = int(input())
dp = [0] + [1 for _ in range(n)]
if n > 1:
    dp[2] = 3
for idx in range(3, n + 1):
    """
    2 * 1 타일을 쓰는 경우: idx - 1
    1 * 2 타일을 쓰는 경우: idx - 2
    2 * 2 타일을 쓰는 경우: idx - 2
    """
    dp[idx] = (dp[idx - 1] + dp[idx - 2] + dp[idx - 2]) % 10007
print(dp[n])
