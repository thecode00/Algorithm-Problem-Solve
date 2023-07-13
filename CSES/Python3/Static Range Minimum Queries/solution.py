# https://cses.fi/problemset/task/1647
# This code TLE test#2
# Maybe python cant solve this problem?

import sys
from typing import List

input = sys.stdin.readline
print = sys.stdout.write


class SegmentTree:
    def __init__(self, arr: List[int]) -> None:
        self.arr = arr
        self.tree = [float("inf")] * (len(arr) * 4)

    def build(self, node: int, left: int, right: int) -> None:
        if left == right:   # Leaf node
            self.tree[node] = self.arr[left]
        else:
            mid = (left + right) // 2
            self.build(node * 2, left, mid)
            self.build(node * 2 + 1, mid + 1, right)
            # Merge left, right child
            self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, node: int, left: int, right: int, start: int, end: int) -> int:
        if start <= left and right <= end:
            return self.tree[node]
        elif end < left or right < start:
            return float("inf")
        else:
            mid = (left + right) // 2
            min_left = self.query(node * 2, left, mid, start, end)
            min_right = self.query(node * 2 + 1, mid + 1, right, start, end)
            return min(min_left, min_right)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
min_tree = SegmentTree(arr)
min_tree.build(1, 0, len(arr) - 1)
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(f"{min_tree.query(1, 0, len(arr) - 1, a, b)}\n")
