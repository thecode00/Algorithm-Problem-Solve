# https://cses.fi/problemset/task/1193

from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
move = "RLDU"

height, width = map(int, input().split())
board = [list(input().rstrip()) for _ in range(height)]
previous_move = [[0 for _ in range(width)] for _ in range(height)]
ay = ax = by = bx = -1

for y in range(height):  # Find "A", "B" position
    for x in range(width):
        if board[y][x] == "A":
            ay = y
            ax = x
        elif board[y][x] == "B":
            by = y
            bx = x

queue = deque()
queue.append((ay, ax))  # Start point
board[ay][ax] = "#"
while queue:    # BFS
    cur_y, cur_x = queue.popleft()
    for idx in range(4):
        new_y, new_x = cur_y + dy[idx], cur_x + dx[idx]
        if (0 <= new_y < height and 0 <= new_x < width and (board[new_y][new_x] == "." or board[new_y][new_x] == "B")):
            board[new_y][new_x] = "#"   # Check visited
            queue.append((new_y, new_x))
            previous_move[new_y][new_x] = idx

if (board[by][bx] == "#"):  # If "A" and "B" connected
    print("YES")
    path = []
    while (ay != by or ax != bx):
        index = previous_move[by][bx]
        path.append(move[index])
        by -= dy[index]
        bx -= dx[index]
    print(len(path))
    for idx in range(len(path) - 1, -1, -1):
        print(path[idx], end="")
else:   # "A" and "B" not connected
    print("NO")
