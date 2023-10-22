# https://school.programmers.co.kr/learn/courses/30/lessons/142085


import heapq


def solution(n, k, enemy):
    if k >= len(enemy):  # 무적권이 스테이지보다 많아서 무조건 깨는경우
        return len(enemy)

    heap = []
    answer = 0
    total = 0
    for idx in range(len(enemy)):
        total += enemy[idx]
        if n >= total:
            # 힙큐에서 최대값을 먼저 빼기위해 음수로 전환해서 push함
            heapq.heappush(heap, -enemy[idx])
            answer += 1
        elif k > 0:
            # 힙큐에 push, pop을 같이해야하는경우 heappushpop을 쓰는게 빠름
            total -= -heapq.heappushpop(heap, -enemy[idx])
            k -= 1
            answer += 1
        else:   # 남은 병사, 무적권이 없을때 무의미한 탐색을 막기
            return answer
    return answer
