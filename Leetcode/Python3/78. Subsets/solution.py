# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(result, index):
            answer.append(result[:])
            for idx in range(index, len(nums)):
                result.append(nums[idx])
                dfs(result, idx + 1)
                result.pop()

        dfs([], 0)
        return answer
