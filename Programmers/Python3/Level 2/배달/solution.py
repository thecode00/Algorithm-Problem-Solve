# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
from bisect import bisect_left, bisect_right
INF = float("inf")


def solution(N, road, K):
    answer = 0
    distance = [INF] * (N + 1)  # 각 마을까지의 최소거리를 저장할 리스트
    maps = [[] for _ in range(N + 1)]
    for start, end, cost in road:
        maps[start].append((end, cost))
        maps[end].append((start, cost))

    q = []
    # 시작 노드로 가기위한 거리를 0으로 설정한다음 큐에 삽입
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 처리된적 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in maps[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는게 거리가 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    distance.sort()  # 이진탐색을위한 정렬
    # 배달가능한 최대거리의 인덱스 + 1을 반환하여 인덱스를 배달가능갯수로 변환시킴
    return bisect_right(distance, K)
