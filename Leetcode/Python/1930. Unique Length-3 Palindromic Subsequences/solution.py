# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        used_letter = set()
        count = 0

        # Find the index of the side letters (first and last occurrence of the same letter)
        # and calculate the count of unique letters between these side letters.
        for idx, letter in enumerate(s):
            if letter not in used_letter:
                right = s.rindex(letter)
                middle_letter = set()

                for i in range(idx + 1, right):
                    if s[i] not in middle_letter:
                        count += 1
                        middle_letter.add(s[i])
                used_letter.add(letter)

        return count


class Solution:  # Optimized
    def countPalindromicSubsequence(self, s: str) -> int:
        used_letter = set()
        count = 0

        for idx, letter in enumerate(s):
            if letter not in used_letter:
                right = s.rindex(letter)

                count += len(set(s[idx + 1: right]))
                used_letter.add(letter)

        return count
