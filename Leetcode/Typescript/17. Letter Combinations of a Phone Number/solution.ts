// https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

function dfs(
  index: number,
  result: string[],
  phonePad,
  digits: string,
  cur: string[]
) {
  if (index === digits.length) {
    result.push(cur.join(""));
    return;
  }

  for (const char of phonePad[digits[index]]) {
    cur.push(char);
    dfs(index + 1, result, phonePad, digits, cur);
    cur.pop();
  }
}

function letterCombinations(digits: string): string[] {
  if (digits.length === 0) {
    return [];
  }

  const phonePad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
  };

  const result: string[] = [];
  dfs(0, result, phonePad, digits, []);
  return result;
}
