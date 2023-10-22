# https://programmers.co.kr/learn/courses/30/lessons/12940

import math


def solution(n, m):
    # return [math.gcd(n, m), math.lcm(n, m)]   왜 lcm이 없다고 뜨는지 모르겠음
    answer = math.gcd(n, m)
    return [answer, (n * m) // answer]
