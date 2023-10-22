# https://www.acmicpc.net/problem/12865


import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # 물품 개수, 최대 무게
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
items = [list(map(int, input().split())) for _ in range(n)]

# dp[y][x]는 아이템을 y개 가지고있고 최대무게가 x일때 물건 가치의 최대값
for y in range(1, n + 1):
    w, v = items[y - 1]  # 무게, 가치
    for x in range(1, k + 1):
        if x - w >= 0:
            # dp[y - 1][x]는 y아이템을 고르지않은 경우
            # dp[y - 1][x - w] + v는 y아이템을 고른 경우, 두 경우를 비교
            dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - w] + v)
        else:
            # y아이템의 무게가 현재 최대무게 x보다 무거울때 y아이템을 고르지않은 경우를 가져옴
            dp[y][x] = dp[y - 1][x]
print(dp[n][k])


# dp를 1차원으로 사용하는 방법 (탑 다운방식)
dp = [0 for _ in range(k + 1)]

for w, v in items:
    for idx in range(k, 0, -1):
        if idx - w >= 0:
            dp[idx] = max(dp[idx], dp[idx - w] + v)
        else:
            break
print(dp[k])
