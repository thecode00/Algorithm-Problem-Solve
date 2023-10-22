# https://www.acmicpc.net/problem/14226


from collections import deque
import sys

input = sys.stdin.readline

target = int(input())
visit = [0] * 1001

queue = deque()
queue.append((1, 0))

while queue:
    now, clip = queue.popleft()
    if now == target:
        print(visit[now])
        print(visit)
        break
    num = now - 1
    if 0 <= num < 1001 and visit[num] == 0:
        queue.append((num, clip))
        visit[num] = visit[now] + 1
    if clip > 0:  # 클립보드에 이모티콘이 있을때
        queue.append((now, now))
        visit[now] += 1
        queue.append((now + clip, clip))
        visit[now + clip] = visit[now] + 1
    else:
        queue.append((now, now))
        visit[now] += 1
