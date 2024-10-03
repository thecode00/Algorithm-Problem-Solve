// https://bigfrontend.dev/problem/roman-numerals-to-integer

/**
 * @param {string} str - roman numeral string
 * @returns {number} integer
 */
function romanToInteger(str) {
  const romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let total = 0;

  for (let idx = 0; idx < str.length; idx++) {
    const curValue = romanMap[str[idx]];
    const nextValue = romanMap[str[idx + 1]] || 0;

    if (curValue >= nextValue) {
      total += curValue;
    } else {
      total -= curValue;
    }
  }

  return total;
}
