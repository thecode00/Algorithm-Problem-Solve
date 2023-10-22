# https://school.programmers.co.kr/learn/courses/30/lessons/64062

from collections import deque


def solution(stones, k):
    window = deque()
    max_cross = float("inf")
    left = 0
    for right, val in enumerate(stones):
        # window내에 val보다 작은값들을 모두 pop해서 항상 window[0]에 현재 범위의 최대값이 있도록 만든다
        while window and window[-1] < val:
            window.pop()
        window.append(val)

        if right < k - 1:
            continue
        # 현재 범위를 건널수있는 최대친구수와 비교
        max_cross = min(max_cross, window[0])

        if stones[left] == window[0]:
            window.popleft()
        left += 1
    return max_cross
