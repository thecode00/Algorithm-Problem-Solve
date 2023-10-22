# https://cses.fi/problemset/task/1667


from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
connect = [[] for _ in range(m + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

path = dict()
path[1] = 1
queue = deque()
queue.append(1)
while queue:
    cur = queue.popleft()
    for node in connect[cur]:
        if node not in path:
            path[node] = cur    # Save previous node
            queue.append(node)

if m not in path:   # Network not connected
    print("IMPOSSIBLE")
else:
    result = [m]
    while m != 1:
        result.append(path[m])
        m = path[m]
    print(len(result))
    print(" ".join(map(str, result[::-1])))
