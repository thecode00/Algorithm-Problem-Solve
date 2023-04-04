# https://leetcode.com/problems/boats-to-save-people/description/


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        count = 0
        while left <= right:
            # If boat can carry heaviest people and lightest people move left pointer
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count
