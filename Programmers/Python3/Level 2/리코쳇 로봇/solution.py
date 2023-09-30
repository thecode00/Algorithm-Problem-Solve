# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque


def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dist = [[-1] * len(board[0]) for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "R":
                dist[y][x] = 0
                queue = deque()
                queue.append((x, y))
                while queue:
                    cur_x, cur_y = queue.popleft()
                    for idx in range(4):
                        new_x, new_y = cur_x, cur_y
                        # 벽이나 장애물에 부딫히기 전까지 계속 이동
                        while 0 <= new_x + dx[idx] < len(board[0]) and 0 <= new_y + dy[idx] < len(board) and board[new_y +
                                                                                                                   dy[idx]][new_x + dx[idx]] != "D":
                            new_x += dx[idx]
                            new_y += dy[idx]
                        if not (new_x != cur_x and new_y != cur_y) and dist[new_y][new_x] == -1:
                            queue.append((new_x, new_y))
                            dist[new_y][new_x] = dist[cur_y][cur_x] + 1
                            if board[new_y][new_x] == "G":  # 목표에 도달
                                return dist[new_y][new_x]
    # 목표에 도달 불가능
    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
