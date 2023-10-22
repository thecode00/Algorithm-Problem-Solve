# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=study-plan&id=algorithm-ii

# Ref: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length - 1

        while start <= end:
            mid = (start + end) >> 1

            if nums[mid] == target:
                return mid
            # left rotated  ex. 3 4 5 1 2
            #                      mid
            if nums[mid] > nums[start]:
                if nums[start] <= target and nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            # right rotated  ex. 5 1 2 3 4
            #                       mid
            else:
                if nums[end] >= target and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1  # If target not exist return -1
