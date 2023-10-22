# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]: # Runtime: 54 ms
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        return nums
    def runningSum(self, nums: List[int]) -> List[int]: # Runtime: 39 ms 
        total = 0
        answer = []
        for n in nums:
            total += n
            answer.append(total)
        return answer