# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:  # Optimization
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if (mid % 2 == 0 and nums[mid + 1] == nums[mid]) or (mid % 2 != 0 and nums[mid - 1] == nums[mid]):
                start = mid + 1
            else:
                end = mid
        return nums[start]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    end = mid - 1
                elif nums[mid] == nums[mid + 1]:
                    start = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    end = mid - 1
                else:
                    return nums[mid]
            print(mid, start, end)
            if start == end:
                return nums[start]

        return nums[0]
