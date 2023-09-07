# https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3


import heapq


def solution(land):
    for y in range(1, len(land)):
        # 전 열에 있는 값들을 힙에 삽입
        heap = []
        for idx, x in enumerate(land[y - 1]):
            # 파이썬의 힙은 최소힙이므로 최대힙으로 바꾸기위해 음수로 변환
            heapq.heappush(heap, (-x, idx))

        for x in range(len(land[0])):
            prev_max_num, prev_max_index = heapq.heappop(heap)
            # 같은열을 연속으로 못밟으므로 그 다음으로 큰수를 가져옴
            if prev_max_index == x:
                temp_num, temp_index = prev_max_num, prev_max_index
                prev_max_num, prev_max_index = heapq.heappop(heap)
                heapq.heappush(heap, (temp_num, temp_index))
            prev_max_num *= -1
            land[y][x] += prev_max_num
            heapq.heappush(heap, (-prev_max_num, prev_max_index))
    return max(land[-1])
