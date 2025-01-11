// https://leetcode.com/problems/construct-k-palindrome-strings/description

function canConstruct(s: string, k: number): boolean {
  if (s.length < k) {
    return false;
  }

  if (s.length === k) {
    return true;
  }

  const letterCounter = new Map<string, number>();
  let palindromeCount = 0;

  for (const letter of s) {
    letterCounter.set(letter, (letterCounter.get(letter) || 0) + 1);
  }

  // A palindrome allows for one odd-count character, so minimum number of palindrome is an odd-count number
  for (const count of letterCounter.values()) {
    if (count % 2 !== 0) {
      palindromeCount += 1;
    }
  }

  return palindromeCount <= k;
}
