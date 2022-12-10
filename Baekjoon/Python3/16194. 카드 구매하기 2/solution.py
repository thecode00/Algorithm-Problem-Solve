"""
https://www.acmicpc.net/problem/16194
관련 문제: https://www.acmicpc.net/problem/11052
"""


import sys

input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))
dp = [0] + [p for p in price]

for idx in range(1, n + 1):
    for i in range(1, idx + 1):
        dp[idx] = min(dp[idx], dp[idx - i] + price[i - 1])
print(dp[n])
