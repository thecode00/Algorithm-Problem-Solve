# https://www.acmicpc.net/problem/10844


import sys

input = sys.stdin.readline
mod = 1000000000

n = int(input())
""""
dp[y][x]는 끝자리가 x으로 끝나는 길이가 y인 계단수 개수
dp를 각 자리수만큼 만들지않고 2개만 만들어서 슬라이딩 윈도 기법으로 공간을 아낄수있다.
출처: https://sihyungyou.github.io/baekjoon-10844/
"""
dp = [[0 for _ in range(10)], [0] + [1 for _ in range(9)]]

for idx in range(n - 1):
    for i in range(10):
        dp[0][i], dp[1][i] = dp[1][i], 0
    for i in range(10):
        # 끝이 n인 계단수는 끝부분 앞자리가 n - 1, n + 1임
        if i - 1 >= 0:
            dp[1][i] += dp[0][i - 1] % mod
        if i + 1 < 10:
            dp[1][i] += dp[0][i + 1] % mod
print(sum(dp[1]) % mod)
