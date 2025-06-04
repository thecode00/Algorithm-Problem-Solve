// https://leetcode.com/problems/valid-number/description/

function isNumber(s: string): boolean {
  const p = /^([+-]?((\.\d+)|(\d+\.?\d*)|(\d+))([eE][+-]?\d+)?)$/;
  return p.test(s);
}
