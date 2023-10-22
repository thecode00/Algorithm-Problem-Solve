# https://www.acmicpc.net/problem/11966


import sys

input = sys.stdin.readline

n = int(input())
n_bin = bin(n)[2:]  # 파이썬은 2진수에 0b를 붙이므로 제거
if n_bin.count("1") == 1:
    print("1")
else:
    print("0")