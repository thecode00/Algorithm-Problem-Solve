# https://codeforces.com/problemset/problem/1374/C

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    length = int(input())
    s = input().rstrip()
    left = []
    move = 0
    for p in s:
        if p == "(":
            left.append("(")
        else:
            if not left:    # When left is blank
                move += 1
            else:   # When left parenthesis is remain they can make bracket
                left.pop()
    print(move)
