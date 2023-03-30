# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import defaultdict


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(game_board, table):
    length = len(game_board)
    answer = 0
    blocks = defaultdict(int)

    for y in range(length):
        for x in range(length):
            if table[y][x] == 1:
                table[y][x] = 0
                stack = [(x, y)]
                point = []
                while stack:
                    cur_x, cur_y = stack.pop()
                    point.append((cur_x - x, cur_y - y))    # 블록들의 좌표들을 일정하게 만들기위해 처음좌표를 0, 0으로 초기화
                    for idx in range(4):
                        nx, ny = cur_x + dx[idx], cur_y + dy[idx]
                        if 0 <= nx < len(table[0]) and 0 <= ny < length and table[ny][nx] != 0:
                            stack.append((nx, ny))
                            table[ny][nx] = 0
                blocks[tuple(point)] += 1   # 튜플은 불변성을 가지고있어서 딕셔너리의 키로 사용가능
    answer += find(game_board, blocks)
    for _ in range(3):
        game_board = rotate(game_board)
        answer += find(game_board, blocks)
    return answer


def find(game_board, blocks):
    length = len(game_board)
    score = 0
    for y in range(length):
        for x in range(length):
            if game_board[y][x] == 0:
                game_board[y][x] = 1
                stack = [(x, y)]
                point = []
                while stack:
                    cur_x, cur_y = stack.pop()
                    point.append((cur_x - x, cur_y - y))    # 블록들의 좌표들을 일정하게 만들기위해 처음좌표를 0, 0으로 초기화
                    for idx in range(4):
                        nx, ny = cur_x + dx[idx], cur_y + dy[idx]
                        if 0 <= nx < length and 0 <= ny < length and game_board[ny][nx] != 1:
                            stack.append((nx, ny))
                            game_board[ny][nx] = 1  # 임시로 방문처리
                cur_block = tuple(point)
                if cur_block in blocks and blocks[cur_block] > 0:
                    score += len(point)
                    blocks[cur_block] -= 1
                else:   # 해당 빈칸에 넣을수있는 블록이 없는경우 방문처리했던 좌표들을 되돌려놔야함
                    for px, py in point:
                        game_board[py + y][px + x] = 0

    return score

# Ref: https://shoark7.github.io/programming/algorithm/rotate-2d-array
def rotate(game_board):  # 보드 회전 함수
    length = len(game_board)
    new_board = [[0 for _ in range(length)] for _ in range(length)]
    for y in range(length):
        for x in range(length):
            new_board[x][length - y - 1] = game_board[y][x]
    # print("new", new_board)
    return new_board


# 테스트용
print(
    solution(
        [[1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0]],
        [[1, 0, 0, 1, 1, 0],
         [1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 0]]))

print(solution([[1, 0], [0, 1]], [[0, 0], [0, 0]]))
