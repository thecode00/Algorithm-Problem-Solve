# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        word = {}
        used_word = set()
        for idx in range(len(pattern)):
            ptrn_word, s_word = pattern[idx], s[idx]
            if ptrn_word in word and word[ptrn_word] != s_word:
                return False
            elif ptrn_word not in word and s_word in used_word:
                return False
            word[ptrn_word] = s_word
            used_word.add(s_word)
        return True
