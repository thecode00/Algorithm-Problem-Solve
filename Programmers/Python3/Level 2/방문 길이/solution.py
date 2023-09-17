# https://school.programmers.co.kr/learn/courses/30/lessons/49994

from collections import defaultdict


def solution(dirs):
    visited = defaultdict(set)
    x, y = 0, 0
    for dir in dirs:
        new_x, new_y = x, y
        if dir == "U":
            new_y += 1
        elif dir == "D":
            new_y -= 1
        elif dir == "R":
            new_x += 1
        else:
            new_x -= 1
        # 경로가 유효하다면 양 좌표가 시작점인 경로를 추가
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            visited[(x, y)].add((new_x, new_y))
            visited[(new_x, new_y)].add((x, y))
            x, y = new_x, new_y
    # 양 좌표가 시작점인 경로를 추가했으므로 2로 나눔
    return sum(len(s) for s in visited.values()) // 2


def solution(dirs):  # 내 코드보다 짧은 코드, Ref: https://velog.io/@letgodchan0/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2
