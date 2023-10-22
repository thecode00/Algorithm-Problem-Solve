# https://www.acmicpc.net/problem/1976


import sys

input = sys.stdin.readline

n = int(input())  # 도시 수
m = int(input())  # 여행계획 도시 수


def find_parent(parent, num):  # 부모노드를 찾는 함수
    if parent[num] != num:
        parent[num] = find_parent(parent, parent[num])
    return parent[num]


city = [num for num in range(n)]
for idx in range(n):
    connect = list(map(int, input().split()))
    for i in range(n):
        if connect[i] == 1:  # 연결되있는 도시와 합침
            p_idx, p_i = find_parent(city, idx), find_parent(city, i)
            if p_idx > p_i:
                city[p_idx] = p_i
            else:
                city[p_i] = p_idx

plan = list(map(int, input().split()))
check = city[plan[0] - 1]  # 부모 노드 체크용
for p in plan:
    if check != city[p - 1]:
        print("NO")
        break
else:  # for문이 break없이 종료됐을때 실행 됨
    print("YES")
