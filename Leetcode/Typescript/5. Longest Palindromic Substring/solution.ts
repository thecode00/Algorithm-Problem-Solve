// https://leetcode.com/problems/longest-palindromic-substring/description/

function longestPalindrome(s: string): string {
  let maxLeft = 0,
    maxRight = 0,
    idx = 0;

  while (idx < s.length) {
    // Skip duplicate char
    while (0 < idx && idx < s.length && s[idx - 1] == s[idx]) {
      idx += 1;
    }

    let left = idx - 1,
      right = idx;

    while (right < s.length && s[idx] == s[right]) {
      right += 1;
    }

    while (left >= 0 && right < s.length && s[left] == s[right]) {
      left -= 1;
      right += 1;
    }

    if (maxRight - maxLeft < right - left) {
      maxRight = right;
      maxLeft = left;
    }
    idx += 1;
  }

  return s.substring(maxLeft + 1, maxRight);
}
