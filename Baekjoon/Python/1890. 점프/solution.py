# https://www.acmicpc.net/problem/1890


import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for y in range(n):
    for x in range(n):
        # dp[y][x]가 0이라면 현재 경로에 길이 없다는 것이므로 패스함
        if board[y][x] == 0 or dp[y][x] == 0:
            continue
        if x + board[y][x] < n:
            dp[y][x + board[y][x]] += dp[y][x]
        if y + board[y][x] < n:
            dp[y + board[y][x]][x] += dp[y][x]
print(dp[n - 1][n - 1])
print(dp)
