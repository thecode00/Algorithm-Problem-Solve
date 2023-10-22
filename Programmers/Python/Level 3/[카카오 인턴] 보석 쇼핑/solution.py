# https://school.programmers.co.kr/learn/courses/30/lessons/67258
# 투 포인터를 사용해서 푼 방식

from collections import defaultdict


def solution(gems):
    jewel_types = len(set(gems))    # 진열되어있는 보석 종류 수
    count = defaultdict(int)
    answer = []
    left = 0
    for right, jewel in enumerate(gems):
        count[jewel] += 1
        if len(count) == jewel_types:
            # left ~ right범위에있는 보석종류가 진열되어있는 보석종류와 같은지 확인, 만약 같다면 범위를 최대한 좁게 만듬
            while left <= right and len(count) == jewel_types:
                answer.append((left + 1, right + 1))
                count[gems[left]] -= 1
                if count[gems[left]] == 0:
                    del count[gems[left]]
                left += 1
    # 범위 길이순, 시작위치순으로 정렬
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]
