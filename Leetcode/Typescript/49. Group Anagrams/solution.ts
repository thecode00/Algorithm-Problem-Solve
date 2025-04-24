// https://leetcode.com/problems/group-anagrams/description/

function groupAnagrams(strs: string[]): string[][] {
  const wordMap = new Map<string, string[]>();

  for (const word of strs) {
    const key = word.split("").sort().join("");

    if (!wordMap.has(key)) {
      wordMap.set(key, []);
    }
    wordMap.get(key)!.push(word);
  }

  return Array.from(wordMap.values());
}

function groupAnagrams(strs: string[]): string[][] {
  const anagramMap = new Map<string, string[]>();

  for (const s of strs) {
    const key = anagramToSortkey(s);

    if (!anagramMap.has(key)) {
      anagramMap.set(key, []);
    }
    anagramMap.get(key)!.push(s);
  }

  return Array.from(anagramMap.values());
}

function anagramToSortkey(str: string): string {
  const key = Array.from(str);

  key.sort();

  return key.join("");
}
