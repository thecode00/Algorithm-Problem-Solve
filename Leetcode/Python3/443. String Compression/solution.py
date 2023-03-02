# https://leetcode.com/problems/string-compression/


from re import S
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        for idx in range(len(chars) - 1, -1, -1):   # Search from right to left
            count += 1
            if idx == 0 or chars[idx] != chars[idx - 1]:
                if count != 1:  # If count == 1 dont need append length
                    str_count = str(count)
                    for i in range(len(str_count)):
                        chars.insert(idx + i + 1, str_count[i])
                count = 0   # Reset count
            else:
                chars.pop(idx)
        return len(chars)


class Solution:  # Use two pointer
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        while right < len(chars):   # Ex. a, a, b, b, b, c, c, left = 0, right = 0
            chars[left] = chars[right]
            count = 1
            # Move to the right until meet another character
            while right < len(chars) - 1 and chars[right] == chars[right + 1]:  # left = 0, right = 1
                count += 1
                right += 1
            if count > 1:   # If the count is more than 1, add characters group length  left = 1, right = 1
                str_count = str(count)
                for s in str_count:
                    chars[left + 1] = s
                    left += 1
            # Move left, right index to not compressed index    left = 2, right = 2
            left += 1
            right += 1
        return left
