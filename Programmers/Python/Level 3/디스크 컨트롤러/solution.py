# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs):
    # job scheduling문제 배정된 작업중 가장 빨리끝나는 작업을 처리하는 그리디로 해결가능
    # 작업이 요청순서대로 온다는 조건이없어서 정렬
    jobs.sort()
    heap = []
    # 완료한 작업수, 현재 시간, 총 작업시간, 힙에 적재된 작업수
    complete = cur_time = total = loaded = 0
    while complete < len(jobs):
        # 힙에 현재 요청이 들어온 작업들을 넣음
        for idx in range(loaded, len(jobs)):
            start, length = jobs[idx]
            if start <= cur_time:
                heapq.heappush(heap, [length, start])
                loaded += 1
            else:
                break

        if heap:
            length, start = heapq.heappop(heap)
            total += cur_time + length - start
            cur_time += length
            complete += 1
        else:
            cur_time += 1

    return total // len(jobs)
