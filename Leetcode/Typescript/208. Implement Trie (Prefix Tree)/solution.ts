// https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode {
  children = new Map<string, TrieNode>();
  complete = false;
  constructor() {}
}

class Trie {
  root = new TrieNode();

  constructor() {}

  insert(word: string): void {
    let cur = this.root;

    for (const char of word) {
      if (!cur.children.has(char)) {
        cur.children.set(char, new TrieNode());
      }
      cur = cur.children.get(char);
    }

    cur.complete = true;
  }

  search(word: string): boolean {
    let cur = this.root;

    for (const char of word) {
      if (!cur.children.has(char)) {
        return false;
      }
      cur = cur.children.get(char);
    }

    return cur.complete;
  }

  startsWith(prefix: string): boolean {
    let cur = this.root;

    for (const char of prefix) {
      if (!cur.children.has(char)) {
        return false;
      }
      cur = cur.children.get(char);
    }

    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
