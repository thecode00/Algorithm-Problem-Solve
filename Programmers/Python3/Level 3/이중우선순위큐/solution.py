# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from bisect import bisect_left
from collections import deque


def solution(operations):
    queue = deque()
    for oper in operations:
        cmd, num = oper.split()
        num = int(num)
        # 이진탐색으로 들어갈 인덱스찾아서 삽입
        if cmd == "I":
            idx = bisect_left(queue, num)
            queue.insert(idx, num)
        elif queue:  # 큐가 비어있지않을때만 값 추출
            if num == 1:
                queue.pop()
            else:
                queue.popleft()

    return [queue[-1], queue[0]] if queue else [0, 0]
