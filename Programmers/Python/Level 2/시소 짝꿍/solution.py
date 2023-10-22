# https://school.programmers.co.kr/learn/courses/30/lessons/152996#

from itertools import combinations
from collections import Counter


def solution(weights):
    weight_count = Counter(weights)
    count = 0
    # 1:1 계산
    for c in weight_count.values():
        # n개에서 2개를 꺼내는 조합의 공식: n * (n - 1) // 2
        count += c * (c - 1) // 2

    for w in weights:
        # 1:2, 2:3, 3:4비율 계산
        for i in range(1, 4):
            # **주의: /가 아닌 //를 해버리면 int형으로 변환되면서 문제가 생김
            torque = (w * (i + 1)) / i
            count += weight_count[torque]

    return count
