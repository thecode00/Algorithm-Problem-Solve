"""
https://codeforces.com/problemset/problem/1734/C
Time complexity: O(N ^ 2)
** PyPy 3
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    total = 0
    S, T = set(i for i in range(1, n + 1)), set()
    for idx, value in enumerate(input().strip()):
        if value != "0":
            T.add(idx + 1)
    delete_set = S - T
    for num in range(1, n + 1):
        if not delete_set:
            break
        for mul in range(1, n + 1):
            smallest = num * mul
            if not delete_set or smallest > n or smallest in T:
                break
            if smallest in delete_set:
                total += num
                delete_set.remove(smallest)

    print(total)
