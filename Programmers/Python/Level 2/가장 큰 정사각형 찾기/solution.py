# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            # board[y][x]는 board[y][x]가 오른쪽 끝인 정사각형의 최대 길이
            if y != 0 and x != 0 and board[y][x] != 0:
                board[y][x] = min(board[y - 1][x], board[y][x - 1], board[y - 1][x - 1]) + 1
            answer = max(answer, board[y][x])
    # print(board)
    return answer ** 2
