# https://leetcode.com/problems/longest-palindrome/?envType=study-plan&id=level-1


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        # Check odd count in longest paildrome, it allows only one odd count
        odd = True  
        length = 0
        for key in count.keys():
            num = count[key]
            if odd and num % 2 != 0: # If num is first odd count add length odd count
                length += num
                odd = False
            elif num >= 2:  
                length += num // 2 * 2
        return length
