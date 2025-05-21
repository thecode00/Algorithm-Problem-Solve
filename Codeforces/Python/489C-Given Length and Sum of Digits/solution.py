"""
https://codeforces.com/problemset/problem/489/C
Time Complexity: O(N)
"""

import sys

input = sys.stdin.readline

m, s = map(int, input().split())
min_number, max_number = "", ""

if (m > 1 and s <= 0) or m * 9 < s:
    print("-1 -1")
else:
    def can(m: int, s: int) -> bool:
        return s <= 9 * m

    temp_s = s
    for idx in range(m):
        for n in range(10):
            if can(m - idx - 1, temp_s - n):
                if idx == 0 and m > 1 and n == 0:
                    continue
                min_number += str(n)
                temp_s -= n
                break

    temp_s = s
    for idx in range(m):
        insert_number = min(9, temp_s)
        max_number += str(insert_number)
        temp_s -= insert_number

    print(f"{min_number} {max_number}")
