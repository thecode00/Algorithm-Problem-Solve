# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
from operator import index


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            # 현재문자가 이미 사용된적있다면 그 문자가 마지막으로나온 인덱스 + 1을 start지점으로 지정한다
            # start가 뒤로 가는것을 방지하기 위해 start <= usedChar[s[i]]를 체크한다
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                # maximum length can only be increased when a new letter is appear 
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength