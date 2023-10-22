# https://leetcode.com/problems/most-common-word/


from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Use regular expression, Use the re.sub() function to replace non-word characters to spaces.
        # ^\w mean not word character
        words = [
            word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned
        ]
        # print(Counter(words).most_common())      
        return Counter(words).most_common(1)[0][0]
