// https://leetcode.com/problems/valid-parentheses/description/

function isValid(s: string): boolean {
  const parenthesis = { "}": "{", "]": "[", ")": "(" },
    stack: string[] = [];

  for (const p of s) {
    if (!parenthesis[p]) {
      stack.push(p);
    } else if (stack.length === 0 || stack.pop() !== parenthesis[p]) {
      return false;
    }
  }

  return stack.length === 0 ? true : false;
}
