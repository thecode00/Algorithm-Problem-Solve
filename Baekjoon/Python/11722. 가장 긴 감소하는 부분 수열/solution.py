# https://www.acmicpc.net/problem/11722


import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
# 모든 자리수에 최소길이인 1을 할당
dp = [1 for _ in range(n)]

for idx in range(1, n):
    for i in range(idx):
        if sequence[idx] < sequence[i]:
            dp[idx] = max(dp[idx], dp[i] + 1)
print(max(dp))
