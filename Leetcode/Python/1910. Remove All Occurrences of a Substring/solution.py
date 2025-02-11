# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description

class Solution:  # Use stack, Time complexity(n * m)
    def removeOccurrences(self, s: str, part: str) -> str:
        char_stack = []

        for char in s:
            char_stack.append(char)

            if len(char_stack) < len(part):
                continue

            # bottleneck
            if "".join(char_stack[-len(part):]) == part:
                for _ in range(len(part)):
                    char_stack.pop()

        return "".join(char_stack)
