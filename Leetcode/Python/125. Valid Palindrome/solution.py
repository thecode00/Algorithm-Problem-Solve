# https://leetcode.com/problems/valid-palindrome/description/
# Time complexity: O(N)


import re


class Solution:  # Two pointer
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            # Find index of alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:  # Check palindrome
                return False
            left += 1
            right -= 1
        return True  # Checked all string return True


class Solution:  # Slicing
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]
