# https://school.programmers.co.kr/learn/courses/30/lessons/181187

import math


def solution(r1, r2):   # 처음 풀이: x ^ 2 + y ^ 2 = r ^ 2 공식대로만 품
    count = 0
    r1pow = r1 ** 2
    r2pow = r2 ** 2

    for x in range(r2 + 1):
        xpow = x ** 2
        y2 = math.isqrt(r2pow - xpow)
        count += y2
        if x < r1:
            y1 = math.sqrt(r1pow - xpow)

            # 경계선에 있는것도 포함해야하므로 따로 처리
            if y1 == int(y1):
                count -= y1 - 1
            else:
                count -= int(y1)

    return 4 * count
