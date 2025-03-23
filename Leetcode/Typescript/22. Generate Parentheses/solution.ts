// https://leetcode.com/problems/generate-parentheses/description/

function generateParenthesis(n: number): string[] {
  const result: string[] = [];

  search(n, n, [], result);
  return result;
}

function search(
  open: number,
  close: number,
  currentString: string[],
  result: string[]
) {
  if (open < 0 || open > close) {
    return;
  }

  if (open === 0 && close === 0) {
    result.push(currentString.join(""));
    return;
  }

  currentString.push("(");
  search(open - 1, close, currentString, result);
  currentString.pop();

  currentString.push(")");
  search(open, close - 1, currentString, result);
  currentString.pop();
}
