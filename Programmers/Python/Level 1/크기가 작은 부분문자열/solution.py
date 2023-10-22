# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    count = 0
    for left in range(len(t) - len(p) + 1):
        right = left + len(p)
        if int(t[left:right]) <= int(p):
            count += 1
    return count
