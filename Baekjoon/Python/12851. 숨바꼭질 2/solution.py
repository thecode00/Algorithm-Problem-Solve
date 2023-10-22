# https://www.acmicpc.net/problem/12851

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())   # 수빈, 동생 위치
fast_time, way = 100001, 0    # 가장빨리 도착한 시간, 방법
visit_time = [0] * fast_time
queue = deque()
queue.append(n)
while queue:
    pos = queue.popleft()
    time = visit_time[pos]
    if pos == k:
        fast_time = time
        way += 1
        continue
    for num in [pos - 1, pos + 1, pos * 2]:
        if 0 <= num < fast_time and (visit_time[num] == 0 or visit_time[num] == time + 1):
            queue.append(num)
            visit_time[num] = time + 1
print(f"{fast_time}\n{way}")    # fString 방법 문자열에 변수넣기 가능
