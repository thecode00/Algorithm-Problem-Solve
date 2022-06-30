# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    # 맵 크기가 세로 가로 길이가 다를수도 있기때문에 세로, 가로길이를 따로 저장
    length_h = len(maps)
    length_w = len(maps[0])
    check = [[-1] * length_w for _ in range(length_h)]

    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    q = deque()
    check[0][0] = 1  # 시작 부분
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for idx in range(4):    # 상하좌우 탐색
            ny = y + dy[idx]
            nx = x + dx[idx]
            if 0 <= ny and ny < length_h and 0 <= nx and nx < length_w:
                if check[ny][nx] == -1 and maps[ny][nx] != 0:  # 탐색된적 없고 벽이 아니라면
                    q.append((ny, nx))
                    check[ny][nx] = check[y][x] + 1
    return check[-1][-1]
