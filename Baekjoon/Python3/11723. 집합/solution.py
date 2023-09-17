# https://www.acmicpc.net/problem/11723

import sys

input = sys.stdin.readline
# 비트의 위치로 숫자를 기억, 만약 n이 존재하면 2 ^ n의 비트를 1로 만드는 형식
bitmask = 0

for _ in range(int(input())):
    s = input().rstrip().split()
    cmd = s[0]
    if len(s) > 1:
        num = int(s[1])
        bit_num = (1 << num)
    if cmd == "add":
        bitmask |= bit_num
    elif cmd == "check":
        if bitmask & bit_num:
            print(1)
        else:
            print(0)
    elif cmd == "remove":
        bitmask &= ~bit_num
    elif cmd == "toggle":
        bitmask ^= bit_num

    elif cmd == "all":
        # 2 ^ 0 비트를 고려해서 비트 21개가 필요
        bitmask = int("0b" + ("1" * 21), 2)
    else:
        bitmask = 0
