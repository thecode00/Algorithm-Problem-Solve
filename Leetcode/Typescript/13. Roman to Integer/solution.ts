// https://leetcode.com/problems/roman-to-integer/description/

function romanToInt(s: string): number {
  const romanMap: { [key: string]: number } = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let total = 0;

  for (let idx = 0; idx < s.length; idx++) {
    const curValue = romanMap[s[idx]];
    const nextValue = romanMap[s[idx + 1]] || 0;

    if (curValue >= nextValue) {
      total += curValue;
    } else {
      total -= curValue;
    }
  }

  return total;
}
