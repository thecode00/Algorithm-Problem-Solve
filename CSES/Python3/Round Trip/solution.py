# https://cses.fi/problemset/task/1669/


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):  # Make graph
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n + 1)


def dfs(start):
    stack = [(start, -1)]
    while stack:
        cur, before = stack.pop()
        if visited[cur] != -1:
            continue
        visited[cur] = before
        for next in graph[cur]:
            if visited[cur] == next:    # Previous city
                continue
            if visited[next] == -1:  # Visit not visited city
                stack.append((next, cur))
            else:   # Found cycle print path
                path = [next]
                while next != cur:
                    path.append(cur)
                    cur = visited[cur]
                path.append(next)
                print(len(path))
                print(" ".join(map(str, path)))
                return True
    return False


flag = False
for i in range(1, n + 1):
    if visited[i] == -1:
        flag = dfs(i)
        if flag:    # If dfs found cycle stop search
            break
else:
    print("IMPOSSIBLE")
