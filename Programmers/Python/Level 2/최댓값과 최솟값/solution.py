# https://school.programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    s = list(map(int, s.split()))
    max_value, min_value = max(s), min(s)

    return f'{min_value} {max_value}'
