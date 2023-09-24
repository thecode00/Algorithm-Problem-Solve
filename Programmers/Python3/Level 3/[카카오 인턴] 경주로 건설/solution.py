# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque


def solution(board):
    length = len(board)
    # **3차원 dp에 대해 처음 알았다 Ref: https://jie0025.tistory.com/312
    visited = [[[False] * 4 for _ in range(length)] for _ in range(length)]  # 방향별 방문 확인용 3차원 배열
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # x좌표, y좌표, 도로의 진행방향(0: 상, 1: 우, 2: 하, 3: 좌, 5: 시작지점), 현재 루트의 비용
    queue = deque([(0, 0, 5, 0)])
    min_cost = float("inf")
    while queue:
        cur_x, cur_y, direction, cost = queue.popleft()
        if cur_x == length - 1 and cur_y == length - 1:
            min_cost = min(min_cost, cost)
        for idx in range(4):
            new_x, new_y = cur_x + dx[idx], cur_y + dy[idx]
            if 0 <= new_x < length and 0 <= new_y < length and board[new_y][new_x] != 1:
                if direction == idx or direction == 5:    # 직선
                    new_cost = cost + 100
                else:   # 방향을 꺾으면 해당칸에 코너(500)1개와 다음 칸으로가는 직선(100)칸 비용
                    new_cost = cost + 600
                # 현재방향으로 방문하지 않은 좌표거나 새로운 비용이 현재 최소비용보다 적을경우
                if not visited[new_y][new_x][idx] or new_cost <= board[new_y][new_x]:
                    queue.append((new_x, new_y, idx, new_cost))
                    board[new_y][new_x] = new_cost
                    visited[new_y][new_x][idx] = True  # 도로 진행방향 방문처리
    return min_cost


# TEST
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
