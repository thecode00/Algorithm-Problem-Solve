# https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import Counter

# TODO: Optimize cpde


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = Counter()
        for right in range(len(s)):
            count[s[right]] += 1

            most = count.most_common(1)[0][1]
            if (right - left) - most == k:
                result = max(result, right - left)
            elif (right - left) - most > k:
                count[s[left]] -= 1
                left += 1
        return right - left
