# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 비슷한 문제: https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150

import itertools


def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    num = 1
    y, x = -1, 0    # 시작 좌표
    while n > 0:
        for _ in range(n):  # 아래 방향
            y += 1
            answer[y][x] = num
            num += 1
        n -= 1
        for _ in range(n):  # 오른쪽 방향
            x += 1
            answer[y][x] = num
            num += 1
        n -= 1
        for _ in range(n):  # 위 방향
            y -= 1
            x -= 1
            answer[y][x] = num
            num += 1
        n -= 1
    # 2차원 리스트 평탄화
    return list(itertools.chain.from_iterable(answer))


def solution(n):    # 삼각형 그리기 중복제거 버전
    answer = [[0] * i for i in range(1, n + 1)]
    num = 1
    y, x = -1, 0    # 시작 좌표
    move_size = n
    for i in range(n):
        for _ in range(move_size):
            if i % 3 == 0:  # 아래 방향
                y += 1
            elif i % 3 == 1:    # 오른쪽 방향
                x += 1
            else:    # 위 방향
                y -= 1
                x -= 1
            answer[y][x] = num
            num += 1

        move_size -= 1
    # 2차원 리스트 평탄화
    return list(itertools.chain.from_iterable(answer))
