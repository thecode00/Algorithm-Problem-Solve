# https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import Counter


class Solution:  # Optimized
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        used_alpha = {}
        max_len = 0

        for right in range(len(s)):
            if s[right] not in used_alpha:
                used_alpha[s[right]] = 1
            else:
                used_alpha[s[right]] += 1

            length = right - left + 1
            if max(length - used_alpha.value()) <= k:
                max_len = max(max_len, length)
            else:
                used_alpha[s[left]] -= 1
                if used_alpha[s[left]] == 0:
                    del used_alpha[s[left]]
                left += 1

        return max_len


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
