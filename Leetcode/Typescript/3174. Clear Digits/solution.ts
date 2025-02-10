// https://leetcode.com/problems/clear-digits/description

function clearDigits(s: string): string {
  const strStack: string[] = [];

  for (let idx = 0; idx < s.length; idx++) {
    if (isNaN(s[idx] as any)) {
      strStack.push(s[idx]);
    } else {
      strStack.pop();
    }
  }
  return strStack.join("");
}
