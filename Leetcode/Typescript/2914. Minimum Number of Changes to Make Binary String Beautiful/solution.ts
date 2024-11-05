// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description

function minChanges(s: string): number {
  let changeCount = 0;
  // Divide string minimum even length and check it needs change
  for (let idx = 0; idx < s.length; idx += 2) {
    changeCount += s[idx] !== s[idx + 1] ? 1 : 0;
  }
  return changeCount;
}
