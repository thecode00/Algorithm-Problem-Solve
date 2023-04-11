# https://www.acmicpc.net/problem/10164

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())    # 행, 열, O격자

dp = [[0 for _ in range(m)] for _ in range(n)]


def search(start_y, end_y, start_x, end_x):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if y == 0 or x == 0:
                dp[y][x] = 1
                continue
            dp[y][x] = dp[y - 1][x] + dp[y][x - 1]


if k == 0:
    search(0, n, 0, m)
else:
    k -= 1  # 0-index로 바꿈
    y, x = k // m, k % m
    # 오른쪽과 아래로만 이동이 가능하므로 k의 위치를 기준으로 왼쪽위 사각형부분과 오른쪽 아래 사각형부분만 계산하면 됨
    search(0, y + 1, 0, x + 1)
    search(y, n, x, m)


print(dp[n - 1][m - 1])
