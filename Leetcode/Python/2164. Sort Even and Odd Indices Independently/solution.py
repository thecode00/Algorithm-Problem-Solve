# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Extract even, odd index elements and sort
        odd, even = [], []

        for idx in range(len(nums)):
            if idx % 2 == 0:
                even.append(nums[idx])
            else:
                odd.append(nums[idx])

        odd.sort(reverse=True)
        even.sort()

        # Insert elements
        even_idx = odd_idx = 0

        for idx in range(0, len(nums), 2):
            nums[idx] = even[even_idx]
            even_idx += 1

        for idx in range(1, len(nums), 2):
            nums[idx] = odd[odd_idx]
            odd_idx += 1
        return nums
