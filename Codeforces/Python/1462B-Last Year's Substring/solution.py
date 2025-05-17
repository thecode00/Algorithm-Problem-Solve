# https://codeforces.com/problemset/problem/1462/B

import sys

input = sys.stdin.readline

t = int(input())


def is_substring(s: str, target: str) -> bool:
    return (
        s[:4] == target or
        s[:3] + s[-1:] == target or
        s[:2] + s[-2:] == target or
        s[:1] + s[-3:] == target or
        s[-4:] == target
    )


for _ in range(t):
    n = int(input())
    s = input().rstrip()

    print("YES" if is_substring(s, "2020") else "NO")
