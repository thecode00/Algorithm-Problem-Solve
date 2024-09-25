// https://leetcode.com/problems/valid-palindrome/description/

function isPalindrome(s: string): boolean {
  const isAlnum = /[0-9a-zA-Z]/; // For check alphabet, number
  let left = 0,
    right = s.length - 1;

  while (left < right) {
    // Skip space
    while (left < right && !isAlnum.test(s[left])) {
      left += 1;
    }
    while (left < right && !isAlnum.test(s[right])) {
      right -= 1;
    }

    if (s[left].toLowerCase() != s[right].toLowerCase()) {
      return false;
    }
    left += 1;
    right -= 1;
  }

  return true;
}
