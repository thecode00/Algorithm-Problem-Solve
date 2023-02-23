# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# Ref: https://github.com/onlybooks/algorithm-interview

def solution(m, n, board):
    board = [list(s) for s in board]
    answer = 0
    while True:
        match = set()
        # 인덱스에서 벗어나는걸 막기위해 m - 1, n - 1까지만 탐색
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j+1] != "#":
                    match.add((i, j))
                    match.add((i + 1, j))
                    match.add((i, j + 1))
                    match.add((i + 1, j + 1))

        if len(match) == 0:  # 지워지는 블록이 없으면 멈춤
            break
        answer += len(match)
        for i, j in match:
            board[i][j] = "#"
        # 떨어지는 블록 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
