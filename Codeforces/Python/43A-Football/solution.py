# https://codeforces.com/problemset/problem/43/A

from collections import defaultdict
import sys

input = sys.stdin.readline

score_dict = defaultdict(int)
for _ in range(int(input())):
    team = input().rstrip()
    score_dict[team] += 1
# key=score_dict.get returns the key with the largest value in the dictionary
print(max(score_dict, key=score_dict.get))
