# https://www.acmicpc.net/problem/4796

import sys

input = sys.stdin.readline

index = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    total = 0
    q, r = divmod(V, P)
    # (휴가에 들어갈수있는 연속일수 * 연속일수중 캠핑장을 사용가능한 일수) + 남은 일수중 최대한 캠핑장을 사용가능한 일수를 넣음
    total += q * L + min(r, L)
    print(f"Case {index}: {total}")
    index += 1
