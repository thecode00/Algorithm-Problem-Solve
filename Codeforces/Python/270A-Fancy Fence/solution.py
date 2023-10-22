# https://codeforces.com/problemset/problem/270/A

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    angle = int(input())
    """
    Minimum regular polygon angle is 60degree (Triangle)
    and regular polygon exterior angle alway 360degree
    So check 360degree divide by exterior angle
    """
    if angle >= 60 and 360 % (180 - angle) == 0:
        print("YES")
    else:
        print("NO")
