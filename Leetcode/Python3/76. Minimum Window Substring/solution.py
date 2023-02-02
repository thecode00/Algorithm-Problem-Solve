# https://leetcode.com/problems/minimum-window-substring/


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sub_length = len(t)
        sub_char = Counter(t)
        # t = set(t)
        left = start = end = 0

        # When you slice 0 ~ n need [n:n + 1] so left index use 0-index right index use 1-index
        for right, val in enumerate(s, 1):
            sub_length -= sub_char[val] > 0     # False == 0, True == 1
            sub_char[val] -= 1

            if sub_length == 0:
                # while left < right and sub_char[s[left]] < 0:
                #     if s[left] in t:
                #         sub_char[s[left]] += 1
                #     left += 1

                while left < right and sub_char[s[left]] < 0:
                    sub_char[s[left]] += 1
                    left += 1
                if not end or end - start >= right - left:
                    end, start = right, left
                # Move left one space to exclude the current char after completing length calculation
                sub_char[s[left]] += 1
                sub_length += 1
                left += 1
        return s[start:end]
