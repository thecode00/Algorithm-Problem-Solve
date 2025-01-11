# https://leetcode.com/problems/construct-k-palindrome-strings/description

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        letter_count = defaultdict(int)
        palindrome_count = 0

        for letter in s:
            letter_count[letter] += 1

        # A palindrome allows for one odd-count character, so the minimum number of characters required for a palindrome is an odd number
        for count in letter_count.values():
            if count % 2 != 0:
                palindrome_count += 1

        return palindrome_count <= k
