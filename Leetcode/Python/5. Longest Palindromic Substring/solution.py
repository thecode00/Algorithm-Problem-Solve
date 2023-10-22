# https://leetcode.com/problems/longest-palindromic-substring/
# Ref: https://leetcode.com/problems/longest-palindromic-substring/solutions/151144/bottom-up-dp-two-pointers/?orderBy=most_votes

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        max_len = 0
        longest_palindrome_start = 0

        for idx in range(len(s)):
            right = idx
            # s ~ right - 1 = same s[idx] character palindrome
            while right < len(s) and s[right] == s[idx]:
                right += 1

            left = idx - 1
            # Find palindrome not same character s[idx]
            while left >= 0 and s[left] == s[right]:
                left -= 1
                right += 1
            # [left + 1 ~ right - 1] is palindrome
            length = right - left - 1
            if max_len < length:
                max_len = length
                longest_palindrome_start = left + 1
        return s[longest_palindrome_start: longest_palindrome_start + max_len]
