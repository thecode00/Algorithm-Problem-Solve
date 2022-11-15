# https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline

n = int(input())
computer = [[] for _ in range(n + 1)]
virus_computer = {1: True}  # 1번 컴퓨터는 항상 감염
for _ in range(int(input())):
    start, end = map(int, input().split())
    # 양방향 연결
    computer[start].append(end)
    computer[end].append(start)


# DFS
stack = [1]
while stack:
    now = stack.pop()
    for com in computer[now]:
        if com not in virus_computer:
            virus_computer[com] = True
            stack.append(com)
print(len(virus_computer.values()) - 1)  # 1번컴퓨터를 뺌
