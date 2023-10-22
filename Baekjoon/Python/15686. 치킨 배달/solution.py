# https://www.acmicpc.net/problem/15686

from itertools import combinations
import sys
from typing import List, Tuple

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# 치킨집과 집 좌표 구하기
chicken, house = [], []
for y in range(n):
    for x in range(n):
        if city[y][x] == 2:
            chicken.append((x, y))
        elif city[y][x] == 1:
            house.append((x, y))


# 현재 치킨집 조합들의 치킨거리를 구함
def check(combi: List[Tuple[int, int]], houses: List[Tuple[int, int]]) -> int:
    total = 0
    for hx, hy in houses:
        chicken_dist = float("inf")
        for cx, cy in combi:
            chicken_dist = min(chicken_dist, abs(hx - cx) + abs(hy - cy))
        total += chicken_dist
    return total


distance = float("inf")
for c in combinations(chicken, m):
    distance = min(distance, check(c, house))

print(distance)
