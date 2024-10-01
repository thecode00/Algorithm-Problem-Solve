// https://leetcode.com/problems/valid-anagram/description/

function isAnagram(s: string, t: string): boolean {
  const newS = Array.from(s).sort().join("");
  const newT = Array.from(t).sort().join("");

  return newS === newT;
}
