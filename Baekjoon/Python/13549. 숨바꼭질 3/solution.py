# https://www.acmicpc.net/problem/13549

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
visit = [False] * 100001
queue = deque()
queue.append((n, 0))

while queue:
    pos, time = queue.popleft()
    if pos == k:
        print(time)
        break
    num = pos * 2
    # 시작위치가 0일때 무한반복하므로 0체크
    if 0 <= num < 100001 and not visit[num] and num != 0:
        visit[num] = True
        # 2배로 이동하는게 무조건 이득이므로 큐의 왼쪽에 추가
        queue.appendleft((num, time))
    for num in [pos - 1, pos + 1]:
        if 0 <= num < 100001 and not visit[num]:
            queue.append((num, time + 1))
            visit[num] = True
