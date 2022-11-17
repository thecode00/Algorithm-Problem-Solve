# https://www.acmicpc.net/problem/13913

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
visit = [-1] * 100001
visit[n] = n
queue = deque()
queue.append((n, 0))
while queue:
    pos, time = queue.popleft()
    if pos == k:
        print(time)
        path = []  # 경로 리스트
        now = k
        path.append(now)
        while now != n:
            # 방문체크를 이전경로를 넣어서 체크했기때문에 경로를 따라가면서 path에 추가
            path.append(visit[now])
            now = visit[now]
        print(" ".join(map(str, path[::-1])))
        break
    for num in [pos + 1, pos - 1, pos * 2]:
        if 0 <= num < 100001 and visit[num] == -1:
            visit[num] = pos  # 방문리스트에 이전경로를 넣어서 체크함
            queue.append((num, time + 1))
