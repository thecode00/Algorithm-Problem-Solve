# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    q = []
    time = 0
    for scov in scoville:
        heapq.heappush(q, scov)
    while len(q) >= 2:
        if q[0] >= K:   # 가장 작은 스코빌이 k를 넘으면 멈춤
            break
        time += 1
        fir = heapq.heappop(q)  # 가장 안매운스코빌
        sec = heapq.heappop(q)  # 두번째로 안매운 스코빌
        heapq.heappush(q, fir + sec * 2)
    if q[0] < K:    # K를 만드는게 불가능할경우 -1
        answer = -1
    else:
        answer = time
    return answer
