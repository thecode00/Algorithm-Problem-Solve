# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height)  - 1
        l_max, r_max = height[left], height[right]
        # They will meet max value of height
        while left > right:
            l_max, r_max = max(l_max, height[left]), max(r_max, height[right])
            print(l_max, r_max)
            # l_max <= r_max means that you can make a hole as high as l_max
            if l_max <= r_max:
                volume += l_max - height[left]
            else:
                volume += r_max - height[right]