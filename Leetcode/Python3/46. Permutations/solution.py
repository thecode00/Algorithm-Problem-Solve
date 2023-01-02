# https://leetcode.com/problems/permutations/

# DFS
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        result = []

        def dfs(numbers: List[int]) -> None:
            if len(result) == len(nums):
                answer.append(result[:])  # If not use copy slice answer list save blank list
                # answer.append(result)
                return
            for idx in range(len(numbers)):
                cur_numbers = numbers[:]  # If not use copy slice del will affect next work
                del cur_numbers[idx]

                result.append(numbers[idx])
                dfs(cur_numbers)
                result.pop()  # Remove calculated number

        dfs(nums)
        return answer


# Use itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations(nums)))