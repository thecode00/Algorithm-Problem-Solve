# https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

from collections import deque


def solution(places):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    def bfs(place, x, y):
        partition = [[-1] * 5 for _ in range(5)]
        # 시작 지점 처리
        partition[y][x] = 0
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for idx in range(4):
                new_x, new_y = cur_x + dx[idx], cur_y + dy[idx]
                # 유효한 좌표, 파티션이 아닐경우, 방문하지 않았던 좌표라면 탐색
                if 0 <= new_x < 5 and 0 <= new_y < 5 and place[new_y][new_x] != "X" and partition[new_y][new_x] == -1:
                    # partition[cur_y][cur_x]가 1라면 partition[new_y][new_x]는 2가될것이기 때문에 1이하일때 새로운 참가자를 만난다면 거리두기가 지켜지지않음
                    if place[new_y][new_x] == "P" and partition[cur_y][cur_x] <= 1:
                        return 0
                    queue.append((new_x, new_y))
                    partition[new_y][new_x] = partition[cur_y][cur_x] + 1

        return 1

    def check_valid(place):
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P" and bfs(place, x, y) == 0:
                    return 0

        return 1

    answer = []
    for place in places:
        answer.append(check_valid(place))

    return answer
