# https://school.programmers.co.kr/learn/courses/30/lessons/131130#


def solution(cards):
    """
    유니온파인드로 그룹을 구별하던것을 최적화한 코드
    """
    parent = list(range(len(cards)))
    visited = [False] * len(cards)

    # 상자그룹을 구하고 그룹별 상자 개수를 구함
    circuit_size = []
    group = 1
    for idx in range(len(cards)):
        if not visited[idx]:
            next = cards[idx] - 1
            size = 0
            while not visited[next]:
                visited[next] = True
                parent[next] = group
                next = cards[next] - 1
                size += 1
            circuit_size.append(size)
            group += 1
    # 상자그룹중 가장 상자가 많은 2개의 그룹을 찾기위해 정렬
    circuit_size.sort()
    return 0 if len(circuit_size) == 1 else circuit_size[-1] * circuit_size[-2]


def solution(cards):
    parent = list(range(len(cards)))
    visited = [False] * len(cards)
    # 유니온 파인드로 그룹 구별

    def find(num):
        if parent[num] != num:
            parent[num] = find(parent[num])
        return parent[num]

    def union(a, b):
        a, b = find(a), find(b)
        if a >= b:
            parent[a] = b
        else:
            parent[b] = a
    circuit_size = []
    # 상자그룹을 구하고 그룹별 상자 개수를 구함
    for idx in range(len(cards)):
        if not visited[idx]:
            next = cards[idx] - 1
            size = 0
            while not visited[next]:
                visited[next] = True
                union(idx, next)
                next = cards[next] - 1
                size += 1
            circuit_size.append(size)
    # 상자그룹중 가장 상자가 많은 2개의 그룹을 찾기위해 정렬
    circuit_size.sort()
    return 0 if len(circuit_size) == 1 else circuit_size[-1] * circuit_size[-2]
