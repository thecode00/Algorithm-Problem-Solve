# https://codeforces.com/problemset/problem/1696/B

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    universe = list(map(int, input().split()))
    answer = 0
    cur_num = 0
    for num in universe:
        # When universe = [5, 0, 3, 0, 1] mex(l = 0, r = 5) -> [2, 2, 2, 2, 2]
        # then mex(l = 0, r = 5) -> [0, 0, 0, 0, 0]
        if answer >= 2:
            print(answer)
            break
        if cur_num == 0 and num != 0:
            answer += 1
            cur_num = num
        elif num == 0:
            cur_num = 0
    else:
        print(answer)
