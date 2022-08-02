# https://leetcode.com/problems/range-sum-query-mutable/

# TODO: Solve
class node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right + 1])