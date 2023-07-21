# https://www.acmicpc.net/problem/10815

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
deck = list(map(int, input().split()))
# 이진탐색을위해 리스트 정렬
deck.sort()

m = int(input())
check = list(map(int, input().split()))


for card in check:
    if bisect_right(deck, card) - bisect_left(deck, card):
        print(1, end=" ")
    else:
        print(0, end=" ")
