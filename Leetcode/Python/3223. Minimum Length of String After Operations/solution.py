# https://leetcode.com/problems/minimum-length-of-string-after-operations/description

class Solution:
    def minimumLength(self, s: str) -> int:
        letter_counter = defaultdict(int)
        minimum_length = 0

        for char in s:
            letter_counter[char] += 1
            # If want delete character least one character to the left and right of index i equal s[i]
            if letter_counter[char] == 3:
                letter_counter[char] = 1

        for count in letter_counter.values():
            minimum_length += count

        return minimum_length
