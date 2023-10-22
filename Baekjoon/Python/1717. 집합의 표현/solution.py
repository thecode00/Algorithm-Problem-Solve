# https://www.acmicpc.net/problem/1717


import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
# 모든 노드를 자기자신을 부모로 설정
node = [num for num in range(n + 1)]

# 부모 루트를 찾는 함수
def find_parent(parent, num):
    if parent[num] != num:
        parent[num] = find_parent(parent, parent[num])
    return parent[num]


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        # 부모루트가 같다면 같은 집합안에 있는 것
        if find_parent(node, a) == find_parent(node, b):
            print("YES")
        else:
            print("NO")
    else:
        # 부모 루트 설정, node의 값을 바꿀때 a, b를 쓰면 안되고 부모루트인 parent_a, parent_b를 대신 써야함
        parent_a, parent_b = find_parent(node, a), find_parent(node, b)
        if parent_a > parent_b:
            node[parent_a] = parent_b
        elif parent_a < parent_b:
            node[parent_b] = parent_a
    print(node)
