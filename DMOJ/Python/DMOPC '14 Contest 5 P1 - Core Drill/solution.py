# https://dmoj.ca/problem/dmopc14c5p1

import math
import sys

input = sys.stdin.readline

r = int(input())    # Radius
h = int(input())    # Height

print((math.pi * (r ** 2) * h) / 3)
