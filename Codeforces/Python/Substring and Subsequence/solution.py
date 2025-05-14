# https://codeforces.com/problemset/problem/1989/B

from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    subsequence = input().rstrip()
    substring = input().rstrip()

    count_subsequence, count_substring = defaultdict(int), defaultdict(int)

    for s in subsequence:
        count_subsequence[s] += 1

    for s in substring:
        count_substring[s] += 1

    count_string = {}

    for s, count in count_subsequence.items():
        count_string[s] = count

    for s, count in count_substring.items():
        if s in count_string:
            count_string[s] = max(count_string[s], count)
        else:
            count_string[s] = count

    print(sum(count_string.values()))
