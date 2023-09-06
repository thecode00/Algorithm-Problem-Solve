# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import defaultdict


def solution(want, number, discount):
    needs = {}  # 원하는 제품의 목록
    for item, num in zip(want, number):
        needs[item] = num
    # print(needs)
    count = 0   # 회원가입 가능한 날짜 수
    window = defaultdict(int)
    # 슬라이딩 윈도우 방식으로 비교
    for idx, val in enumerate(discount):
        window[val] += 1
        if idx >= 9:
            if window == needs:
                # print(window)
                count += 1
            window[discount[idx - 9]] -= 1
            if window[discount[idx - 9]] == 0:
                window.pop(discount[idx - 9])

    return count
