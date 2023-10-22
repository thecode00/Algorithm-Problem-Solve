# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        combis = []
        for o in orders:
            combis += combinations(sorted(o), c)
        count = Counter(combis).most_common()
        for idx in range(len(count)):
            # Counter.most_common은 가장 많이 나온순서대로 정렬된 리스트를 반환하므로 가장앞에있는 빈도수가 max값
            if count[idx][1] == count[0][1] and count[idx][1] >= 2:
                answer.append("".join(count[idx][0]))
            else:
                break
        print(answer)
    return sorted(answer)   # 사전순으로 출력해야므로 정렬
