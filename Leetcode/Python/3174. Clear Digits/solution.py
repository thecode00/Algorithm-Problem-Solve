# https://leetcode.com/problems/clear-digits/description

class Solution:
    def clearDigits(self, s: str) -> str:
        char_stack = []

        for char in s:
            if not char.isdigit():
                char_stack.append(char)
            else:
                char_stack.pop()

        return "".join(char_stack)
