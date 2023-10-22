# https://www.acmicpc.net/problem/10818

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
