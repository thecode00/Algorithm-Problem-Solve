# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # str은 immutable인 객체이기 때문에 방문처리를 위해 리스트로 변환
    maps = [list(m) for m in maps]
    # DFS로 무인도에 있는 음식수 구하기

    def dfs(x, y):
        food = int(maps[y][x])
        stack = [(x, y)]
        maps[y][x] = "X"
        while stack:
            x, y = stack.pop()
            for idx in range(4):
                new_x, new_y = x + dx[idx], y + dy[idx]
                if 0 <= new_x < len(maps[0]) and 0 <= new_y < len(maps) and maps[new_y][new_x] != "X":
                    food += int(maps[new_y][new_x])
                    maps[new_y][new_x] = "X"    # 방문처리
                    stack.append((new_x, new_y))

        return food

    answer = []
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != "X":
                answer.append(dfs(x, y))

    answer.sort()
    # 무인도가 없을때 예외처리
    return answer if answer else [-1]


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
