# https://www.acmicpc.net/problem/11057


import sys

input = sys.stdin.readline
mod = 10007

n = int(input())
dp = [[0 for _ in range(10)], [1 for _ in range(10)]]
# n = 1일때 n % 2 == 1

for idx in range(2, n + 1):
    # i는 끝이 i로 끝나는 오름수를 나타냄
    for i in range(10):
        dp[idx % 2][i] = (dp[(idx + 1) % 2][i]) % mod
        for j in range(i):  # 끝이 i로 끝나므로 i보다 작은 0 ~ j를 range로 잡고 탐색
            dp[idx % 2][i] += (dp[(idx + 1) % 2][j]) % mod

print((sum(dp[n % 2])) % mod)
