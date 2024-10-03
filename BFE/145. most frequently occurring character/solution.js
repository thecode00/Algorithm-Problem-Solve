// https://bigfrontend.dev/problem/most-frequently-occurring-character

/**
 * @param {string} str
 * @returns {string | string[]}
 */
function count(str) {
  const counter = new Map();
  let result = [];
  let mostCommon = 0;

  for (const char of str) {
    // Map의 원소존재 여부 따로 검사없이 쓰는법
    counter.set(char, (counter.get(char) || 0) + 1);

    if (counter.get(char) > mostCommon) {
      result = [];
      mostCommon = counter.get(char);
    }

    if (mostCommon === counter.get(char)) {
      result.push(char);
    }
  }

  return result.length > 1 ? result : result[0];
}
