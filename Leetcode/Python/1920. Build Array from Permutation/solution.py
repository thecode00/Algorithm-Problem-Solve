# https://leetcode.com/problems/build-array-from-permutation/description

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        for idx in range(len(nums)):
            answer[idx] = nums[nums[idx]]
        
        return answer