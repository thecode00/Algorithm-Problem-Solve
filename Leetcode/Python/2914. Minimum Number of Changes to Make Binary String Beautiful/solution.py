# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description

class Solution:  # First solution
    def minChanges(self, s: str) -> int:
        change_count = 0
        # Divide string minimum even length and count min change
        for idx in range(0, len(s), 2):
            zero = s[idx: idx + 2].count("0")
            one = 2 - zero
            change_count += min(zero, one)

        return change_count


class Solution:  # Second solution
    def minChanges(self, s: str) -> int:
        change_count = 0
        # Divide string minimum even length and check it needs change
        for idx in range(0, len(s), 2):
            change_count += s[idx] != s[idx + 1]

        return change_count
