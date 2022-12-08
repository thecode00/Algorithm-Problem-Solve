# https://www.acmicpc.net/problem/2294


import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 종류, 목표 가치
coins = [int(input()) for _ in range(n)]
dp = [0] + [float("inf") for _ in range(k)]  # dp[0]은 자기자신이므로 0을 넣어줌

for idx in range(k + 1):
    for c in coins:
        if idx - c >= 0 and dp[idx] > dp[idx - c] + 1:
            dp[idx] = dp[idx - c] + 1
print(dp[k] if dp[k] != float("inf") else -1)  # 불가능한경우에는 -1출력
