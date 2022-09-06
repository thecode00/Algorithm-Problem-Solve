# https://codeforces.com/problemset/problem/158/B

import math
import sys

input = sys.stdin.readline

n = int(input())
group = list(map(int, input().split()))
taxi = group.count(4)
one, two, three = group.count(1), group.count(2), group.count(3)
taxi += three
if one <= three:
    one = 0
else:
    one -= three
two += math.ceil(one / 2)
print(taxi + math.ceil(two / 2))
