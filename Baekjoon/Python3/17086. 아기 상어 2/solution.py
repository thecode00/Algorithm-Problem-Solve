# https://www.acmicpc.net/problem/17086


# 처음 푼 방식, 6920ms 매우느림
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로 길이
shark_map = [list(map(int, input().split())) for _ in range(n)]
# 북, 남, 서, 동, 북서, 남서, 북동, 남동
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
safe_distance = 0


def bfs(y, x):
    visit = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((y, x))
    while queue:
        now_y, now_x = queue.popleft()
        if shark_map[now_y][now_x] == 1:
            return visit[now_y][now_x]
        for idx in range(8):
            ny, nx = now_y + dy[idx], now_x + dx[idx]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or visit[ny][nx] != 0:
                continue
            queue.append((ny, nx))
            visit[ny][nx] = visit[now_y][now_x] + 1


for y in range(n):
    for x in range(m):
        if shark_map[y][x] == 0:
            safe_distance = max(safe_distance, bfs(y, x))
print(safe_distance)


# 두번째로 푼 방식, 96ms
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로 길이
shark_map = [list(map(int, input().split())) for _ in range(n)]
# 북, 남, 서, 동, 북서, 남서, 북동, 남동
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
safe_distance = 0
visit = [[-1] * m for _ in range(n)]

queue = deque()

for y in range(n):
    for x in range(m):
        if shark_map[y][x] == 1:
            queue.append((y, x))
            visit[y][x] = 0  # 상어를 중심으로 안전거리를 찾을것이기 때문에 0으로 초기화

while queue:
    now_y, now_x = queue.popleft()
    for idx in range(8):
        ny, nx = now_y + dy[idx], now_x + dx[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or visit[ny][nx] != -1:
            continue
        visit[ny][nx] = visit[now_y][now_x] + 1
        queue.append((ny, nx))
        safe_distance = max(safe_distance, visit[ny][nx])
print(safe_distance)
