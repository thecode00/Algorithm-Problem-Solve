# https://leetcode.com/problems/most-common-word/


from collections import Counter
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Use regular expression, Use the re.sub() function to replace non-word characters to spaces.
        # ^\w mean not word character
        words = [
            word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned
        ]
        # print(Counter(words).most_common())
        return Counter(words).most_common(1)[0][0]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()

        # Replacing all non-numeric and non-alphabetic characters with spaces
        p = re.compile("\W+")
        paragraph = re.sub("\W+", " ", paragraph).strip()
        counter = Counter(paragraph.split(" "))
        ban_hash = set(banned)
        for word, _ in counter.most_common():
            if word not in ban_hash:
                return word
        return ""
