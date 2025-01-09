# https://leetcode.com/problems/counting-words-with-a-given-prefix/description

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pattern = re.compile(f"^{pref}")
        count = 0

        for word in words:
            if pattern.match(word):
                count += 1

        return count
