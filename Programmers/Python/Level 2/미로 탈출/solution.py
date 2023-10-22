# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque


def solution(maps):
    dist = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(start_x, start_y, visited):
        queue = deque()
        queue.append((start_x, start_y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for idx in range(4):
                new_x, new_y = cur_x + dx[idx], cur_y + dy[idx]
                if 0 <= new_x < len(
                        maps[0]) and 0 <= new_y < len(maps) and maps[new_y][new_x] != "X" and not visited[new_y][new_x]:
                    visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                    if maps[new_y][new_x] == "S" or maps[new_y][new_x] == "E":
                        dist.append(visited[new_y][new_x])  # 시작점, 탈출점과 레버와의 거리를 저장
                    queue.append((new_x, new_y))
        return dist

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "L":
                dist = bfs(x, y, visited)
                # 레버가 시작점과 탈출점과 이어져있는지 확인
                return sum(dist) if len(dist) == 2 else -1

    return "ERROR: 레버가 없습니다"
