# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:  # Runtime: 220 ms
        start = 0
        end = len(numbers) - 1
        while start <= end:
            total = numbers[start] + numbers[end]
            if total > target:
                end -= 1
            elif total < target:
                start += 1
            else:
                return [start + 1, end + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:  # Runtime: 184 ms
        dic = {}
        for idx, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, idx + 1]
            dic[num] = idx
