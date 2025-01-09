# https://www.acmicpc.net/problem/2447

import sys

input = sys.stdin.readline

n = int(input())


def star(length):
    if length == 3:
        return ["***", "* *", "***"]

    result = []
    prev_star = star(length // 3)

    for line in prev_star:
        result.append(line * 3)

    for line in prev_star:
        result.append(line + ' ' * (length // 3) + line)

    for line in prev_star:
        result.append(line * 3)

    return result


print("\n".join(star(n)))
