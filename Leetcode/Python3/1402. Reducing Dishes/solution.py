# https://leetcode.com/problems/reducing-dishes/
# Ref: https://leetcode.com/problems/reducing-dishes/solutions/563384/java-c-python-easy-and-concise/?orderBy=most_votes
# Time complexity: O(N)

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = prev = 0
        while satisfaction and satisfaction[-1] + prev > 0:  # If total < 0 It's a loss to add
            prev += satisfaction.pop()
            total += prev
        return total
