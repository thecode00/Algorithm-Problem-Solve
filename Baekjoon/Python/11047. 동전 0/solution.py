# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
# 코인이 오름차순으로 입력되므로 코인배열의 끝부분부터 거꾸로 탐색
for idx in range(n - 1, -1, -1):
    count += k // coins[idx]
    k %= coins[idx]
    if k == 0:
        break

print(count)
