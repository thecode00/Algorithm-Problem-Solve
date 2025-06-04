# https://leetcode.com/problems/validate-ip-address/description/

import re


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4_pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
        v6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

        if re.fullmatch(v4_pattern, queryIP):
            for num in queryIP.split("."):
                if num != str(int(num)) or not 0 <= int(num) <= 255:
                    return "Neither"
            return "IPv4"
        elif re.fullmatch(v6_pattern, queryIP):
            return "IPv6"
        else:
            return "Neither"
