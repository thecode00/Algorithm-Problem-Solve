# https://www.acmicpc.net/problem/1018

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
bw = ['B', 'W']


def check_row(color: int, start_y: int, start_x: int) -> int:
    change = 0
    for i in range(8):
        if board[start_y][start_x + i] != bw[color % 2]:
            change += 1
        color += 1  # 색 변경
    return change


def check_board(color: int, start_y: int, start_x: int) -> int:
    total = 0
    for cur_y in range(start_y, start_y + 8):
        total += check_row(color % 2, cur_y, start_x)
        color += 1  # 색 변경
    return total


answer = float("inf")
for y in range(n - 7):
    for x in range(m - 7):
        answer = min(answer, check_board(0, y, x))  # 첫번째 칸이 흑색으로 시작하는 보드 검사
        answer = min(answer, check_board(1, y, x))  # 첫번째 칸이 흰색으로 시작하는 보드 검사

print(answer)
