# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로 길이
maze = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 미로의 최단거리문제는 dfs대신 bfs를 써야함
def bfs():  # 시작위치가 고정이기때문에 매개변수가 필요없음
    queue = deque()  # deque를 써서 큐를 구현함
    queue.append([0, 0])
    while queue:
        now_y, now_x = queue.popleft()
        for idx in range(4):
            ny, nx = now_y + dy[idx], now_x + dx[idx]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or maze[ny][nx] != 1:
                continue
            maze[ny][nx] = maze[now_y][now_x] + 1  # 큐에 넣기전에 방문처리를 해줘야 시간초과가 안남
            queue.append([ny, nx])


bfs()
print(maze[n - 1][m - 1])
