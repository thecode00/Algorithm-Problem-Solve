# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if s < n:
        return [-1]
    q, r = divmod(s, n)
    answer = []
    for _ in range(n):
        answer.append(q)
        if r:
            answer[-1] += 1
            r -= 1

    return answer[::-1]
