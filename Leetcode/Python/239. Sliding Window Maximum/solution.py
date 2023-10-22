# https://leetcode.com/problems/sliding-window-maximum/


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []
        for idx, val in enumerate(nums):
            # Remove element small than current value in the window
            while window and val > nums[window[-1]]:
                window.pop()
            window.append(idx)
            """
            Ex. nums = [0, 1, 2, 3, 4, 5]
            idx = 2, k = 2, window = 0, [1, 2], 3, 4, 5 If window[0] == 0 pop
            idx = 3, k = 2, window = 0, 1, [2, 3], 4, 5 If window[0] == 1 pop
            """
            if window[0] == idx - k:
                window.popleft()
            if idx >= k - 1:
                result.append(nums[window[0]])
        return result
