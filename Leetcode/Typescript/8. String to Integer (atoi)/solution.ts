// https://leetcode.com/problems/string-to-integer-atoi/description/

function myAtoi(s: string): number {
  s = s.trim();

  if (s.length === 0) {
    return 0;
  }

  let index = 0,
    isNegative = false;
  if (s[0] === "+" || s[0] === "-") {
    index += 1;
    if (s[0] === "-") {
      isNegative = true;
    }
  }

  // Read number from left
  let number = 0;
  while (index < s.length) {
    if (!isDigit(s[index])) {
      break;
    }
    number *= 10;
    number += parseInt(s[index]);
    console.log(number, s[index], Number.isNaN(s[index]));
    index += 1;
  }

  if (isNegative) {
    number *= -1;
  }
  // Round number
  number = Math.max(Math.min(number, 2 ** 31 - 1), (-2) ** 31);
  return number;
}

function isDigit(str: string): boolean {
  return /^[0-9]+$/.test(str);
}
