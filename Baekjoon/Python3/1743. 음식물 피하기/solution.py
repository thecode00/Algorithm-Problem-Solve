# https://www.acmicpc.net/problem/1743

from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

n, m, k = map(int, input().split())  # 세로, 가로길이, 쓰레기 개수
trash = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
path = [[0] * m for _ in range(n)]
for _ in range(k):  # 쓰레기 위치 입력받음
    r, c = map(int, input().split())
    path[r - 1][c - 1] = 1


def dfs_recur(y, x):  # 재귀함수를 이용한 dfs
    amount = 1
    path[y][x] = 0
    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or path[ny][nx] != 1:
            continue
        amount += dfs_recur(ny, nx)
    return amount


def dfs(y, x):  # 재귀함수를 사용하지 않은 dfs
    amount = 1
    stack = [(y, x)]
    path[y][x] = 0
    while stack:
        now_y, now_x = stack.pop()
        for idx in range(4):
            ny, nx = now_y + dy[idx], now_x + dx[idx]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or path[ny][nx] != 1:
                continue
            path[ny][nx] = 0
            amount += 1
            stack.append((ny, nx))
    return amount


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    path[y][x] = 0
    amount = 1
    while queue:
        now_y, now_x = queue.popleft()
        for idx in range(4):
            ny, nx = now_y + dy[idx], now_x + dx[idx]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or path[ny][nx] != 1:
                continue
            path[ny][nx] = 0
            amount += 1
            queue.append((ny, nx))
    return amount


for y in range(n):
    for x in range(m):
        if path[y][x] == 1:
            trash = max(trash, dfs(y, x))
print(trash)
