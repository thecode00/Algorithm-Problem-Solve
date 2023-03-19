# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Word:
    def __init__(self) -> None:
        self.complete = False
        self.child = {}


class WordDictionary:

    def __init__(self):
        self.words = Word()

    def addWord(self, word: str) -> None:
        cur = self.words
        for char in word:
            if char not in cur.child:
                cur.child[char] = Word()
            cur = cur.child[char]
        cur.complete = True

    def search(self, word: str) -> bool:
        stack = [(self.words, word)]
        while stack:
            node, w = stack.pop()
            if not w:   # If w is reached to the end, the search is complete
                if node.complete:
                    return True
                else:
                    continue
            char = w[0]

            if char == ".":
                for trie_node in node.child.values():
                    stack.append((trie_node, w[1:]))
                continue

            if char in node.child:
                stack.append((node.child[char], w[1:]))

        return False    # Word not in dictionary

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
