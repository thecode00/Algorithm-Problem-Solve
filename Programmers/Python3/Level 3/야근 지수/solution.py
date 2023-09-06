# https://school.programmers.co.kr/learn/courses/30/lessons/12927

from bisect import bisect_left


def solution(n, works):
    total = sum(works)
    if total <= n:  # 야근전에 모든 일을 다 마칠수있는경우
        return 0

    works.sort()
    # 최대값을 최대한 줄임
    while n:
        max_num = works[-1]
        left = bisect_left(works, max_num)
        for idx in range(left, len(works)):
            n -= 1
            works[idx] -= 1
            if n == 0:
                break

    score = 0
    for num in works:
        score += num ** 2

    return score
