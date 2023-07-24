# https://www.acmicpc.net/problem/2841

from collections import defaultdict
import sys

input = sys.stdin.readline

n, p = map(int, input().split())
guitar = defaultdict(list)
move = 0
for _ in range(n):
    wire, fret = map(int, input().split())
    # 낮은음 연주를 위해 손가락을 움직임
    while guitar[wire] and guitar[wire][-1] > fret:
        move += 1
        guitar[wire].pop()
    # 이미 누르고 있는 프렛 중복 방지
    if guitar[wire] and guitar[wire][-1] == fret:
        continue
    guitar[wire].append(fret)
    move += 1
print(move)
