# https://www.acmicpc.net/problem/1303

import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 가로, 세로 길이
war_map = [list(input().rstrip()) for _ in range(m)]
w_power, b_power = 0, 0


def cal_power(y, x, team):
    if y < 0 or y >= m or x < 0 or x >= n or war_map[y][x] != team:
        return 0
    war_map[y][x] = 1  # 방문처리
    power = 1
    # 상하좌우를 탐색해서 같은팀이 있는지 확인
    power += (
        cal_power(y + 1, x, team)
        + cal_power(y - 1, x, team)
        + cal_power(y, x + 1, team)
        + cal_power(y, x - 1, team)
    )
    return power


for y in range(m):
    for x in range(n):
        if war_map[y][x] == "W":
            w_power += cal_power(y, x, "W") ** 2
        elif war_map[y][x] == "B":
            b_power += cal_power(y, x, "B") ** 2
print(w_power, b_power)
