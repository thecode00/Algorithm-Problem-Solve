# https://www.acmicpc.net/problem/17136
# Ref: https://www.udemy.com/course/comgong_codingtest/

import sys

input = sys.stdin.readline

piece = [0] * 6
paper = [list(map(int, input().split())) for _ in range(10)]
result = 100


def possible(x: int, y: int, size: int) -> bool:
    """paper[y][x]에 size * size인 색종이를 놓을수있는지 확인하는 함수

    Args:
        x, y: 좌표
        size: 색종이의 크기

    Returns:
        색종이를 놓을수있다면 True반환
    """
    if piece[size] >= 5 or x + size > 10 or y + size > 10:
        return False
    for py in range(y, y + size):
        for px in range(x,  x + size):
            if paper[py][px] == 0:
                return False

    return True


def attachAndDetach(x: int, y: int, size: int, off: int) -> None:
    """종이에 색종이를 붙이거나 때는 함수

    Args:
        x, y: 붙일 색종이의 좌상단위치
        size: 붙일 색종이의 크기
        off: 0이면 색종이를 종이에 붙임, 1이면 색종이를 땜
    """
    if off:
        piece[size] -= 1
    else:
        piece[size] += 1
    for py in range(y, y + size):
        for px in range(x, x + size):
            paper[py][px] = off


def search(x: int, y: int) -> None:
    """ 색종이가 몇개 들어가는지 확인하는 함수

    Args:
        x, y: 좌표값
    """
    global result
    if y == 10:
        result = min(result, sum(piece))
    elif x == 10:
        search(0, y + 1)
    elif paper[y][x] == 0:
        search(x + 1, y)
    else:
        for size in range(1, 6):
            # size크기의 색종이를 붙일수있다면 붙인상태의 종이를 탐색해보고 땐 다음 다른크기의 색종이를 탐색
            if possible(x, y, size):
                attachAndDetach(x, y, size, 0)
                search(x + 1, y)
                attachAndDetach(x, y, size, 1)


search(0, 0)
print(-1 if result == 100 else result)
