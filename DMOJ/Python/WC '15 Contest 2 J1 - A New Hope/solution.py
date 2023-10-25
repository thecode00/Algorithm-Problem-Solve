# https://dmoj.ca/problem/wc15c2j1

import sys

input = sys.stdin.readline

n = int(input())
# join() method is a string method that allows you to concatenate elements of an iterable
print(f"A long time ago in a galaxy {', '.join(['far'] * n)} away...")
