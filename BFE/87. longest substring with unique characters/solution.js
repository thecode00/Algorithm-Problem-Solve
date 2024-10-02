// https://bigfrontend.dev/problem/longest-substring-with-unique-characters

/**
 * @param {string} str
 * @return {string}
 */
function longestUniqueSubstr(str) {
  const used = new Set();
  let maxLeft = 0,
    maxLength = 0,
    left = 0;

  for (let right = 0; right < str.length; right++) {
    if (used.has(str[right])) {
      left = right;
      used.clear();
    }

    used.add(str[right]);
    if (right - left + 1 > maxLength) {
      maxLeft = left;
      maxLength = right - left + 1;
    }
  }

  return str.substring(maxLeft, maxLeft + maxLength);
}
