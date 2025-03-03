# https://leetcode.com/problems/partition-array-according-to-given-pivot/description

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return less + equal + greater


class Solution:  # Three pointer
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        answer = [0] * len(nums)

        less = equal = 0

        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        greater = less + equal
        equal = less
        less = 0

        for num in nums:
            if num < pivot:
                answer[less] = num
                less += 1
            elif num == pivot:
                answer[equal] = num
                equal += 1
            else:
                answer[greater] = num
                greater += 1

        return answer
