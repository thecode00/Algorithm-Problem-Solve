# https://www.acmicpc.net/problem/7562


from collections import deque
import sys

input = sys.stdin.readline

dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(int(input())):
    l = int(input())
    queue = deque()
    queue.append(tuple(map(int, input().split())))
    chess = [[0] * l for _ in range(l)]
    target_y, target_x = map(int, input().split())

    while queue:
        now_y, now_x = queue.popleft()
        if now_y == target_y and now_x == target_x:
            print(chess[now_y][now_x])
            break
        for idx in range(8):
            ny, nx = now_y + dy[idx], now_x + dx[idx]
            if 0 <= ny < l and 0 <= nx < l and chess[ny][nx] == 0:
                queue.append((ny, nx))
                chess[ny][nx] = chess[now_y][now_x] + 1
