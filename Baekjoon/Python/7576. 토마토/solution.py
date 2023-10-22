# https://www.acmicpc.net/problem/7576

from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())  # 가로, 세로 길이
tomato = [list(map(int, input().split())) for _ in range(n)]
ripe = True
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

queue = deque()
for y in range(n):  # 큐에 처음에 익은 토마토들의 좌표를 넣음
    for x in range(m):
        if tomato[y][x] == 1:
            queue.append((y, x))

time = -1  # 처음 큐엔 익은 토마토들의 좌표만 있으므로 -1로 초기화
while queue:  # 한번 while루프가 돌때마다 같은날에 익은 토마토들의 좌표를 꺼내고 주변을 익게만듬
    time += 1  # 큐가 비워질때마다 time에 1씩 추가
    for idx in range(len(queue)):
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and tomato[ny][nx] == 0:
                queue.append((ny, nx))
                tomato[ny][nx] = 1


def check_ripe(time):
    for y in range(n):
        for x in range(m):
            if tomato[y][x] == 0:  # 익게할수 없는 토마토가 있을경우 -1을 출력하고 바로 리턴
                print(-1)
                return
    print(time)
    return


check_ripe(time)
