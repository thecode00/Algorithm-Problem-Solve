# https://www.acmicpc.net/problem/1915

import sys

input = sys.stdin.readline

# 다이나믹 프로그래밍, O(NM)
n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
# dp[y][x] = square[y][x]좌표가 우하단인 정사각형의 최대크기
dp = [[0] * m for _ in range(n)]

maxSize = 0
for y in range(n):
    for x in range(m):
        if square[y][x] == "1":
            if y == 0 or x == 0:
                dp[y][x] = 1
            else:
                dp[y][x] = min(dp[y][x - 1],
                               dp[y - 1][x - 1],
                               dp[y - 1][x]) + 1
            maxSize = max(maxSize, dp[y][x])
# dp에는 넓이가아닌 크기가 들어가있으므로 제곱을 해서 넓이를 출력해야함
print(maxSize ** 2)

# 브루트포스, TLE
n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]


def findSquareArea(start_y: int, start_x: int, size: int) -> int:
    area = 0
    for y in range(start_y, start_y + size):
        for x in range(start_x, start_x + size):
            # 정사각형이 될수없는경우 최소크기 1반환
            if y >= n or x >= m or square[y][x] == "0":
                return 1
            area += 1
    # 크기를 1키운 정사각형이 될수있는지 확인
    area = max(area, findSquareArea(start_y, start_x, size + 1))
    return area


maxArea = 0
for y in range(n):
    for x in range(m):
        if square[y][x] == "1":
            maxArea = max(maxArea, findSquareArea(y, x, 1))

print(maxArea)
