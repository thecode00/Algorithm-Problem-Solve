# https://www.acmicpc.net/problem/2293


import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 종류, 목표 가치
dp = [0 for _ in range(k + 1)]
dp[0] = 1
coins = [int(input()) for _ in range(n)]

# for idx in range(1, k + 1):
#     for c in coins:
#         if idx - c > 0:
#             dp[idx] += dp[idx - c]

# 코인가치 c의 배수마다 조합수가 1씩 늘어나는것을 이용
for c in coins:
    for idx in range(1, k + 1):
        if idx - c >= 0:
            dp[idx] += dp[idx - c]
    print(dp)
print(dp[k])
