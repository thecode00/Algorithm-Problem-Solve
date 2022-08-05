# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    # Left to right
    def replaceElements(self, arr: List[int]) -> List[int]: # Runtime: 3940 ms
        for idx in range(len(arr) - 1):
            arr[idx] = max(arr[idx + 1:])
        arr[-1] = -1
        return arr
    # Right to left
    def replaceElements(self, arr: List[int]) -> List[int]: # Runtime: 179 ms
        pre_value = -1
        for idx in range(len(arr) -1, -1, -1):
            arr[idx], pre_value = pre_value, max(arr[idx], pre_value)
        return arr