// https://leetcode.com/problems/group-anagrams/description/

function groupAnagrams(strs: string[]): string[][] {
  const wordMap = new Map<string, string[]>();

  for (const word of strs) {
    const key = word.split("").sort().join("");

    if (!wordMap.has(key)) {
      wordMap.set(key, []);
    }
    wordMap.get(key).push(word);
  }

  return Array.from(wordMap.values());
}
