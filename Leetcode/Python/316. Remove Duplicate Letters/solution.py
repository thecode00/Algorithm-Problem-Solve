# https://leetcode.com/problems/remove-duplicate-letters/


from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, check, stack = Counter(s), set(), []

        for c in s:
            count[c] -= 1
            if c in check:
                continue
            check.add(c)
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                check.remove(stack.pop())
            stack.append(c)
        return "".join(stack)
