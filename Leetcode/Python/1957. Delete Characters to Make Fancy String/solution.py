# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description

class Solution:
    def makeFancyString(self, s: str) -> str:
        str_list = list(s)

        cons_count = 0
        cons_char = ""
        
        for idx, char in enumerate(s):
            if cons_char != char:
                cons_char = char
                cons_count = 1
            else:
                if cons_count >= 2:
                    str_list[idx] = ""
                else:
                    cons_count += 1
        
        return "".join(str_list)
