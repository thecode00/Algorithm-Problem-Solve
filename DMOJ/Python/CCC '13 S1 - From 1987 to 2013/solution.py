# https://dmoj.ca/problem/ccc13s1

import sys

input = sys.stdin.readline

year = int(input()) + 1


def is_distinct_year(str_year: str) -> bool:
    size = len(str_year)
    return len(set(str_year)) == size


while not is_distinct_year(str(year)):
    year += 1

print(year)
