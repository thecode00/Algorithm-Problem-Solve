# https://leetcode.com/problems/valid-mountain-array/

# Ref: https://leetcode.com/problems/valid-mountain-array/discuss/1717377/JavaC%2B%2BPython-EASY-to-go-through-solution-and-EXPLANATION
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end = 0, len(arr) - 1
        if end < 2: # The minimum length of a mountain is 3
            return False
        # Mountain must have at least one ascend and descend
        # So we check for ascend to end - 1 and descend from end to 1
        while start < end - 1 and arr[start] < arr[start + 1]:
            start += 1
        while 1 < end and arr[end] < arr[end - 1]:
            end -= 1
        return start == end