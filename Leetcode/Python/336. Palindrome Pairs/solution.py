# https://leetcode.com/problems/palindrome-pairs/

from collections import defaultdict
from typing import List


class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.word_index = -1
        self.palindrome_index = []


class Solution:
    def __init__(self) -> None:
        self.root = Trie()

    def is_palindrome(self, word: str):
        return word == word[::-1]

    def check_palindrome(self, word: str, index: int):
        result = []
        cur = self.root

        # Check if there is a word with the same prefix as the current word, and rest of current word forms a palindrome.
        # Ex. word = llss, ss
        while word:
            if cur.word_index != -1 and self.is_palindrome(word):
                result.append([index, cur.word_index])
            if word[0] not in cur.children:
                return result
            cur = cur.children[word[0]]
            word = word[1:]

        # Check reversed word exist
        if cur.word_index != -1 and cur.word_index != index:
            result.append([index, cur.word_index])

        # Check if there is a word with the same prefix as the current word and the rest is palindrome
        # Ex. word = ss, llss
        for idx in cur.palindrome_index:
            result.append([index, idx])

        return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        for idx, word in enumerate(words):
            cur = self.root
            for i, c in enumerate(reversed(word)):
                if self.is_palindrome(word[:len(word) - i]):
                    cur.palindrome_index.append(idx)
                cur = cur.children[c]
            cur.word_index = idx

        result = []
        for idx, word in enumerate(words):
            result.extend(self.check_palindrome(word, idx))

        return result
