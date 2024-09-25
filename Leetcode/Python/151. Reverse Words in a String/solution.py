# https://leetcode.com/problems/reverse-words-in-a-string/

# Python string is immutable so need O(N) memory

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        idx = 0

        # Split word
        words = []
        temp = []
        while idx < len(s):
            if s[idx] == " ":
                if not temp:
                    idx += 1
                    continue
                words.append("".join(temp))
                temp.clear()
            else:
                temp.append(s[idx])
            idx += 1

        if temp:
            words.append("".join(temp))

        words.reverse()
        return " ".join(words)
