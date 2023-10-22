# https://school.programmers.co.kr/learn/courses/30/lessons/43162


def find_parent(parent, num):
    if parent[num] != num:
        parent[num] = find_parent(parent, parent[num])
    return parent[num]


def solution(n, computers):
    parent = [num for num in range(n)]
    for idx in range(n):
        for i in range(n):
            if computers[idx][i] == 1:
                # idx와 i컴퓨터의 부모노드를 가져옴
                parent_idx, parent_i = find_parent(parent, idx), find_parent(parent, i)
                if parent_idx > parent_i:
                    parent[idx] = parent_i
                else:
                    parent[i] = parent_idx
    # 양방향연결이지만 문제에서 방향을 한쪽으로만 줘서 for문을 2번돌려 부모노드를 찾음
    for idx in range(n):
        for i in range(n):
            if computers[idx][i] == 1:
                parent_idx, parent_i = find_parent(parent, idx), find_parent(parent, i)
                if parent_idx > parent_i:
                    parent[idx] = parent_i
                else:
                    parent[i] = parent_idx
    return len(set(parent))




