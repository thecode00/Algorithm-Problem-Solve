# https://school.programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    used = set()
    prev = words[0][0]
    for idx in range(len(words)):
        if words[idx][0] != prev or words[idx] in used:
            if (idx + 1) % n != 0:
                person = (idx + 1) % n
                count = (idx + 1) // n + 1
            else:
                person = n
                count = (idx + 1) // n
            return [person, count]
        prev = words[idx][-1]
        used.add(words[idx])
    return [0, 0]
