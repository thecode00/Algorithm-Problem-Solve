# https://leetcode.com/problems/defanging-an-ip-address/


import re


class Solution:  # RegExp
    def defangIPaddr(self, address: str) -> str:
        return re.sub(r"\.", "[.]", address)


class Solution:  # inbuilt method
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
