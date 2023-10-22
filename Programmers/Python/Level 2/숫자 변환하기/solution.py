# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque


def solution(x, y, n):
    visited = [False] * (y + 1)
    visited[x] = True
    queue = deque()
    queue.append((x, 0))
    while queue:
        cur, move = queue.popleft()
        if cur == y:
            return move
        for num in [cur * 3, cur * 2, cur + n]:
            if num <= y and not visited[num]:
                queue.append((num, move + 1))
                visited[num] = True

    return -1


print(solution(10, 40, 5))
print(solution(10, 10000000, 5))
