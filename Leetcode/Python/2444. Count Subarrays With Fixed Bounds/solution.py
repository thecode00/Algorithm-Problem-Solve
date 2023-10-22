# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# Ref: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/?orderBy=most_votes

class Solution:
    # Ex. nums = [3 1 3 5 2 7 5], minK = 1, maxK = 5
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mink_index, maxk_index = None, None
        subarray_index = -1
        count = 0
        for idx, num in enumerate(nums):
            # When idx == 0, subarray_index = -1
            if not minK <= num <= maxK:  # Subarray should only have values greater than minK and less than maxK.
                subarray_index = idx
            # MinK and maxK may be the same, so inspect them separately.
            if num == minK:  # When idx == 1, mink_index = 1
                mink_index = idx
            if num == maxK:  # When idx == 3, maxk_index = 3
                maxk_index = idx
            if mink_index != None and maxk_index != None:
                # Subarray range = subarray_index + 1 ~ min(mink_index, maxk_index)
                # mink_index = 1, maxk_index = 3, subarray_index = -1, subarray = [3 1 3 5], [1 3 5]
                # subarray range = [3 1 3 5] 2 7 5
                count += max(0, min(mink_index, maxk_index) - subarray_index)
        return count
