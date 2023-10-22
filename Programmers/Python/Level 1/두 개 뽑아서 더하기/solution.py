# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    answer = set()  # 증복값을 피하기위해 set로 선언
    # numbers에서 2개씩뽑아서 sum으로 두 원소를 합하고 set에 추가
    for comb in combinations(numbers, 2):
        answer.add(sum(comb))
    return list(sorted(answer))
