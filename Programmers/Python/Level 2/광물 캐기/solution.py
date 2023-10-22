# https://school.programmers.co.kr/learn/courses/30/lessons/172927

import heapq


def solution(picks, minerals):
    answer = 0
    table = {0: {"diamond": 1, "iron": 1, "stone": 1},
             1: {"diamond": 5, "iron": 1, "stone": 1},
             2: {"diamond": 25, "iron": 5, "stone": 1}}
    heap = []
    # 테스트케이스 8번 틀리는이유: 곡괭이가 캘수있는 광물수보다 더 많은 광물수가 존재해서
    for idx in range(0, min(len(minerals), sum(picks) * 5), 5):
        total = [0]
        for m in minerals[idx: idx+5]:
            total[0] += table[2][m]  # 피로도 구별을 위해 돌 곡괭이 기준으로 피로도 측정
            total.append(m)
        total[0] *= -1  # Max_heap을 위해 음수로 저장
        heapq.heappush(heap, total)

    print(heap)

    for idx in range(3):
        while picks[idx] and heap:
            picks[idx] -= 1
            mines = heapq.heappop(heap)[1:]  # 광물목록만 가져옴
            for m in mines:
                answer += table[idx][m]

    return answer
