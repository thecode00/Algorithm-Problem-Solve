# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def dfs(n, board, row):
    count = 0
    if n == row:    # n개의 퀸이 다 배치가 가능하면 1반환
        return 1
    for c in range(n):
        board[row] = c  # board의 각 row마다 column을 체크
        for r in range(row):
            if abs(board[row] - board[r]) == abs(row - r) or board[r] == board[row]:
                break
        else:   # for문에서 break되지않았을때 실행
            count += dfs(n, board, row + 1)
    return count


def solution(n):
    return dfs(n, [0] * n, 0)
