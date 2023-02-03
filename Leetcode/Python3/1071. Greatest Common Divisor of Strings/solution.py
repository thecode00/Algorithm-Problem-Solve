# https://leetcode.com/problems/greatest-common-divisor-of-strings/


from math import lcm


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Ex. str1 = "ABCABC", str2 = "ABC"
        l1, l2 = len(str1), len(str2)   # l1 = 6, l2 = 3
        # First, find gcd of str lengths
        gcd_length = l1 * l2 // lcm(l1, l2)  # gcd(6, 3) = 3
        gcd_str = str1[:gcd_length]  # ABCABC[:3] = ABC
        """
        If str1 and str2 has same divisor gcd * (len(str) // gcd_length) is same str1 or str2
        ABC * 2 = str1, ABC * 1 = str2
        """
        if str1 == gcd_str * (l1 // gcd_length) and str2 == gcd_str * (l2 // gcd_length):
            return gcd_str
        return ""
