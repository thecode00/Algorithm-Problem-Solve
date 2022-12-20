# https://www.acmicpc.net/problem/4195


import sys

input = sys.stdin.readline


def find_parent(parent, name):
    if parent[name] != name:
        parent[name] = find_parent(parent, parent[name])
    return parent[name]


def union(parent, visit, f1, f2):
    p1, p2 = find_parent(parent, f1), find_parent(parent, f2)
    # 부모노드역할과 총 친구개수를 둘중 한개의 노드에 몰아줘서 계산
    if p1 != p2:
        parent[p1] = p2
        visit[p2] += visit[p1]


t = int(input())  # 테스트케이스 개수
for _ in range(t):
    f = int(input())  # 친구관계 수
    parent = {}
    visit = {}
    for _ in range(f):
        f1, f2 = input().rstrip().split()
        # 처음나오는 친구면 친구 딕셔너리에 넣음
        if f1 not in parent:
            parent[f1] = f1
            visit[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            visit[f2] = 1
        union(parent, visit, f1, f2)
        print(visit[find_parent(parent, f2)])
