# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import defaultdict


def solution(topping):
    chulsu, brother = defaultdict(int), defaultdict(int)
    count = 0

    for t in topping:
        chulsu[t] += 1

    # 끝부분부터 자르면서 토핑 종류 비교
    for cut_idx in range(len(topping) - 1, 0, -1):
        chulsu[topping[cut_idx]] -= 1
        if chulsu[topping[cut_idx]] == 0:
            del chulsu[topping[cut_idx]]

        brother[topping[cut_idx]] += 1

        if len(chulsu) == len(brother):
            count += 1

    return count
