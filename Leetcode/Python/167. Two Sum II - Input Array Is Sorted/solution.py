# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, idx + 1]
            dic[num] = idx

            
class Solution: # Two pointer
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1


class Solution:  # Binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, val in enumerate(numbers):
            start, end = idx + 1, len(numbers) - 1
            temp_target = target - val
            while start <= end:
                mid = start + (end - start) // 2
                if numbers[mid] == temp_target:
                    return [idx + 1, mid + 1]
                elif numbers[mid] > temp_target:
                    end = mid - 1
                else:
                    start = mid + 1
            