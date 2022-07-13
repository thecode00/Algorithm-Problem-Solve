# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split a string s based on space and flip each string
        list_reverse = [string[::-1] for string in list(s.split())]
        # print(list_reverse)
        return " ".join(list_reverse)
