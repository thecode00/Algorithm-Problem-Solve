# https://www.acmicpc.net/problem/1449

import sys

input = sys.stdin.readline

n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
tapes = 0
index = 0

while index < n:
    tapes += 1
    end = holes[index] + l - 1  # 테이프가 커버할수있는 범위
    while index < n and holes[index] <= end:
        index += 1

print(tapes)
