# https://www.acmicpc.net/problem/1182
# Ref: https://seongonion.tistory.com/98

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0


def back_tracking(idx, total):
    global answer

    if idx >= n:
        return

    total += numbers[idx]

    if total == s:
        answer += 1

    # 현재 원소를 포함한 부분수열 탐색
    back_tracking(idx + 1, total)
    # 현재 원소를 포함하지 않는 부분수열 탐샘
    back_tracking(idx + 1, total - numbers[idx])


back_tracking(0, 0)
print(answer)
