# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        for li in sorted(intervals, key=lambda x: x[0]):
            # If overlap last element extend last element
            if answer and li[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], li[1])
            else:   # Not overlaping
                answer.append(li)
        return answer
