# https://school.programmers.co.kr/learn/courses/30/lessons/12985


def solution(n, a, b):  # 계속 2로 나누므로 O(log n)이 되서 문제그대로 -구현해도 됨
    answer = 0

    while a != b:
        answer += 1

        a = sum(divmod(a, 2))
        b = sum(divmod(b, 2))

    return answer
