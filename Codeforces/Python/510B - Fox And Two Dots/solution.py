# https://codeforces.com/problemset/problem/510/B

from collections import deque
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(prev_row: int, prev_col: int, row: int, col: int, target: str):
    visited[row][col] = True

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if 0 <= new_row < n and 0 <= new_col < m and graph[new_row][new_col] == target:
            if visited[new_row][new_col]:
                if (new_row != prev_row or new_col != prev_col):
                    print("Yes")
                    exit()

                continue

            dfs(row, col, new_row, new_col, target)


def bfs(start_row, start_col, target):
    queue = deque()
    queue.append((start_row, start_col, -1, -1))
    visited[start_row][start_col] = True

    while queue:
        row, col, prev_row, prev_col = queue.popleft()
        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]
            if 0 <= new_row < n and 0 <= new_col < m and graph[new_row][new_col] == target:
                if visited[new_row][new_col]:
                    if new_row != prev_row or new_col != prev_col:
                        print("Yes")
                        exit()
                    continue
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, row, col))


for row in range(n):
    for col in range(m):
        if not visited[row][col]:
            bfs(row, col, graph[row][col])
print("No")
