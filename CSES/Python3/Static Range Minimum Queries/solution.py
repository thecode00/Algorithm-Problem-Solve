# https://cses.fi/problemset/task/1647

# TODO: solve
import sys

input = sys.stdin.readline

n, q = map(int, input().split())    # Length of array, number of queries
arr = list(map(int, input().split()))

height = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    height[i] = height[i >> 1] + 1

table = [[-1 for _ in range(n)] for _ in range(height[-1] + 1)]
table[0] = arr

step = 1
for y in range(1, height[-1] + 1):
    for x in range(n):
        if x + step < n:
            table[y][x] = min(table[y - 1][x], table[y - 1][x + step])
        else:
            break
    step <<= 1

for _ in range(q):
    a, b = map(int, input().split())
    # Make to 0-index
    a -= 1
    b -= 1
    row = height[b - a + 1]
    print(min(table[row][a], table[row][b + 1 - (1 << row)]))
